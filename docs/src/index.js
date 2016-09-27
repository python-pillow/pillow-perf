var adapter = require("./chars-adapter");
var data = require("./data/index");

var competition = data[0].competitions[0];

document.addEventListener("DOMContentLoaded", function(){
  adapter.chartForCompetition(
    document.getElementById("chartContainer"),
    competition
  );
});
