require("./stylesheet.css");

var adapter = require("./chars-adapter");
var data = require("./data/index");
var objectAssign = require('object-assign');

// Global chart instance. Should be destroyed every time.
var globalChart = null;
var globalSystem;
var globalCompetition;
var globalPreset;
var globalUnits;

var unitsPresets = {
  seconds: {
    label: 's',
    valuePrecision: 4,
    leftpad: 7,
    reverseDrawOrder: false,
    formatValue: function(time, competition) {
      return time;
    },
    howFaster: function(current, first) {
      return first / current;
    }
  },
  megapixels: {
    label: 'MP/s',
    valuePrecision: 2,
    leftpad: 7,
    reverseDrawOrder: false,
    formatValue: function(time, competition) {
      var size = competition.source.size;
      if (time)
        return size[0] * size[1] / time / 1e6;
    },
    howFaster: function(current, first) {
      return current / first;
    }
  },
  operations: {
    label: 'op/s',
    valuePrecision: 2,
    leftpad: 7,
    reverseDrawOrder: false,
    formatValue: function(time, competition) {
      if (time)
        return 1.0 / time;
    },
    howFaster: function(current, first) {
      return current / first;
    }
  },
}


function partialCompetition(element, competitionName, presetName) {
  var competitions = data.systems[0].competitions;
  var competitors = [];
  var i, competition, preset;

  for (i = 0; i < competitions.length; i++) {
    if (competitions[i].name == competitionName) {
      competition = objectAssign({}, competitions[i]);
      break;
    }
  }
  if ( ! competition) {
    console.log('Competition ' + competitionName + ' is not found.');
    return;
  }

  if (presetName) {
    if (typeof presetName === "string") {
      for (i = 0; i < competition.presets.length; i++) {
        if (competition.presets[i].name == presetName) {
          preset = competition.presets[i].set;
          break
        }
      }
      if ( ! preset) {
        console.log('Preset ' + presetName + ' is not found.');
        return;
      }
    } else {
      preset = presetName;
    }

    for (i = 0; i < competition.competitors.length; i++) {
      var competitor = competition.competitors[i];
      if (preset.indexOf(competitor.name) > -1) {
        competitors.push(competitor);
      }
    }

    competition.competitors = competitors;
  }

  return adapter.chartForCompetition(
    element,
    competition,
    unitsPresets.seconds
  );
}


function applyUnits(units) {
  globalUnits = units;

  if (globalChart) {
    globalChart.destroy();
  }

  globalChart = adapter.chartForCompetition(
    document.getElementById("chart-container"),
    globalCompetition,
    unitsPresets[globalUnits]
  );

  if (globalPreset) {
    adapter.applyPreset(globalChart, globalPreset.set);
  }
}


function createSelect(select, list, callback) {
  var elements = [];
  select.innerHTML = '';

  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var element = document.createElement('a');
    element.href = '#';
    element.innerText = item.title;
    element.addEventListener('click', function(e) {
      e.preventDefault();
    });
    elements.push(element);
    select.appendChild(document.createElement('li')).appendChild(element);
    select.appendChild(document.createTextNode(" "));
    callback(i, element, item);
  }

  function selectItem(n) {
    for (var i = 0; i < elements.length; i++) {
      var element = elements[i];
      element.className = (n == i) ? 'selected' : '';
    }
  }

  return selectItem;
}


function setTopic(parent, topic) {
  for (var i = 0; i < parent.classList.length; i++) {
    var theClass = parent.classList[i];
    if (theClass.substr(0, 'topic__'.length) == 'topic__') {
      parent.classList.remove(theClass);
    }
  }
  if (topic) {
    parent.classList.add('topic__' + topic);
  }
}


function populatePresets(presets) {
  var select = document.getElementById("select-preset");
  var parent = select.parentNode;

  parent.style.display = presets.length ? 'block' : 'none';

  var selectItem = createSelect(select, presets, function(i, element) {
    element.addEventListener('click', applyPreset.bind(null, i));
  });

  function applyPreset(n) {
    var preset = presets[n];
    globalPreset = preset;
    selectItem(n);
    setTopic(parent, preset.topic);
    adapter.applyPreset(globalChart, preset.set);
  }
  return applyPreset;
}


function populateCompetitions(competitions) {
  var select = document.getElementById("select-competition");
  var parent = select.parentNode;
  var info = parent.getElementsByClassName('info')[0];
  
  var selectItem = createSelect(select, competitions, function(i, element) {
    element.addEventListener('click', applyCompetition.bind(null, i));
  });

  function applyCompetition(n) {
    var competition = competitions[n];
    globalCompetition = competition;

    if (globalChart) {
      globalChart.destroy();
    }

    globalChart = adapter.chartForCompetition(
      document.getElementById("chart-container"),
      competition,
      unitsPresets[globalUnits]
    );

    var innerHTML = "";
    if (competition.topic) {
      innerHTML = '<a class="pseudo" href="#' +
        competition.topic + '">More info about operation</a>';
    }
    info.innerHTML = innerHTML;

    selectItem(n);

    setTopic(parent, competition.topic);

    if (competition.presets) {
      var applyPreset = populatePresets(competition.presets);

      for (var i = 0; i < competition.presets.length; i++) {
        if (competition.presets[i].default) {
          applyPreset(i);
          break;
        }
      }
    } else {
      populatePresets([]);
      globalPreset = null;
    }
  }
  return applyCompetition;
}


function populateSystems(systems) {
  var select = document.getElementById("select-system");
  var parent = select.parentNode;
  var info = parent.getElementsByClassName('info')[0];
  
  var selectItem = createSelect(select, systems, function(i, element) {
    element.addEventListener('click', applySystem.bind(null, i));
  });

  function applySystem(n) {
    globalSystem = systems[n];
    var applyCompetition = populateCompetitions(globalSystem.competitions);
    applyCompetition(0);
    
    selectItem(n);

    var innerHTML = "";
    if (globalSystem.OS) {
      innerHTML += "<strong>OS</strong> " + globalSystem.OS + "<br>";
    }
    if (globalSystem.CPU) {
      innerHTML += "<strong>CPU</strong> " + globalSystem.CPU + "<br>";
    }
    info.innerHTML = innerHTML;
  }

  return applySystem;
}


function setupUnits() {
  var topics = document.getElementById('switch-units').getElementsByTagName("a");

  for (var i = 0; i < topics.length; i++) {
    if (topics[i].classList.contains('selected')) {
      globalUnits = topics[i].getAttribute('data-unit');
    }

    topics[i].addEventListener('click', function(e) {
      for (var i = 0; i < topics.length; i++) {
        topics[i].classList.remove('selected');
      }
      this.classList.add('selected');
      applyUnits(this.getAttribute('data-unit'));

      e.preventDefault();
    });
  }
}


document.addEventListener("DOMContentLoaded", function(){

  var applySystem = populateSystems(data.systems);
  setupUnits();
  applySystem(0);
  
});

module.exports = partialCompetition;
