var adapter = require("./chars-adapter");
var data = require("./data/index");

var competition = data[0].competitions[0];


function createSelect(select, list, callback) {
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
  }
}


function populatePresets(chart, presets) {
  var select = document.getElementById("select-preset");
  
  createSelect(select, presets, function(i, element, preset) {
    element.innerText = preset.title;
    element.addEventListener('click', applyPreset.bind(null, i));
  });

  function applyPreset(n) {
    adapter.applyPreset(chart, presets[n].set);
  }
  return applyPreset;
}


document.addEventListener("DOMContentLoaded", function(){
  var chart = adapter.chartForCompetition(
    document.getElementById("chart-container"),
    competition
  );
  var applyPreset = populatePresets(chart, competition.presets);
  applyPreset(4);
});
