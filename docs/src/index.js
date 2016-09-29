var adapter = require("./chars-adapter");
var data = require("./data/index");


function createSelect(select, list, callback) {
  var elements = [];
  select.innerHTML = '';
  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var element = document.createElement('a');
    element.href = '#';
    document.addEventListener('click', function(e) {
      e.preventDefault();
    })
    select.appendChild(document.createElement('li')).appendChild(element);
    callback(i, element, item);
    elements.push(element);
  }

  function selectItem(n) {
    for (var i = 0; i < elements.length; i++) {
      var element = elements[i];
      element.className = (n == i) ? 'selected' : '';
    }
  }

  return selectItem;
}


function populatePresets(chart, presets) {
  var select = document.getElementById("select-preset");
  
  var selectItem = createSelect(select, presets, function(i, element, preset) {
    element.innerText = preset.title;
    element.addEventListener('click', applyPreset.bind(null, i));
  });

  function applyPreset(n) {
    selectItem(n);
    adapter.applyPreset(chart, presets[n].set);
  }
  return applyPreset;
}


function populateCompetitions(competitions) {
  var select = document.getElementById("select-competition");
  
  var selectItem = createSelect(select, competitions, function(i, element, competition) {
    element.innerText = competition.title;
    element.addEventListener('click', applyCompetition.bind(null, i));
  });

  function applyCompetition(n) {
    var competition = competitions[n];
    var chart = adapter.chartForCompetition(
      document.getElementById("chart-container"),
      competition
    );

    selectItem(n);

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


document.addEventListener("DOMContentLoaded", function(){
  
  var applyCompetition = populateCompetitions(data[0].competitions);
  applyCompetition(0);
});
