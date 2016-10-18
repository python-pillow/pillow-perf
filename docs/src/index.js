var adapter = require("./chars-adapter");
var data = require("./data/index");

// Global chart instance. Should be destroyed every time.
var chart = null;


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
    })
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


function populatePresets(chart, presets) {
  var select = document.getElementById("select-preset");
  var parent = select.parentNode;

  parent.style.display = presets.length ? 'block' : 'none';

  var selectItem = createSelect(select, presets, function(i, element) {
    element.addEventListener('click', applyPreset.bind(null, i));
  });

  function applyPreset(n) {
    var preset = presets[n];
    selectItem(n);
    setTopic(parent, preset.topic);
    adapter.applyPreset(chart, preset.set);
  }
  return applyPreset;
}


function populateCompetitions(competitions) {
  var select = document.getElementById("select-competition");
  var parent = select.parentNode;
  
  var selectItem = createSelect(select, competitions, function(i, element) {
    element.addEventListener('click', applyCompetition.bind(null, i));
  });

  function applyCompetition(n) {
    var competition = competitions[n];

    if (chart) {
      chart.destroy();
    }

    chart = adapter.chartForCompetition(
      document.getElementById("chart-container"),
      competition
    );

    selectItem(n);

    setTopic(parent, competition.topic);

    if (competition.presets) {
      var applyPreset = populatePresets(chart, competition.presets);

      for (var i = 0; i < competition.presets.length; i++) {
        if (competition.presets[i].default) {
          applyPreset(i);
          break;
        }
      }
    } else {
      populatePresets(chart, []);
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
    var innerHTML = "";
    var system = systems[n];
    var applyCompetition = populateCompetitions(system.competitions);
    applyCompetition(0);
    
    selectItem(n);

    if (system.OS) {
      innerHTML += "<strong>OS</strong> " + system.OS + "<br>";
    }
    if (system.CPU) {
      innerHTML += "<strong>CPU</strong> " + system.CPU + "<br>";
    }
    info.innerHTML = innerHTML;
  }

  return applySystem;
}


document.addEventListener("DOMContentLoaded", function(){

  var applySystem = populateSystems(data);
  applySystem(0);

});
