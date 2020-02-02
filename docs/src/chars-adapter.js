var Chart = require("chart.js/dist/Chart.js");

Chart.defaults.global.defaultFontColor = 'black';
Chart.defaults.myBar = Chart.defaults.bar;
Chart.controllers.myBar = Chart.controllers.bar.extend({
    // Increase bars width
    getRuler: function(index) {
        var ruler = Chart.controllers.bar.prototype.getRuler.call(this, index);
        ruler.barWidth += 10;
        ruler.barSpacing -= 10;
        return ruler;
    },
    maxForGroup: function(group) {
        var max = null;
        var groups = this.chart.data.groups;
        var datasets = this.chart.data.datasets;
        for (var j = 0; j < groups.length; j++) {
            if (group != groups[j]) {
                continue;
            }
            for (var i = 0; i < datasets.length; i++) {
                var value = datasets[i].data[j];

                if ( ! this.chart.isDatasetVisible(i) || ! value) {
                    continue;
                }
                if (max === null || value > max) {
                    max = value;
                }
            }
        }
        return max;
    },
    calculateBarY: function(index, datasetIndex) {
        var me = this;
        var meta = me.getMeta();
        var yScale = me.getScaleForId(meta.yAxisID);
        var value = Number(me.getDataset().data[index]);

        if (me.chart.data.groups && me.chart.data.groups.length) {
            var group = me.chart.data.groups[index];
            var max = me.maxForGroup(group);

            me = yScale;
            var innerDimension = me.height - (me.paddingTop + me.paddingBottom);
            var range = innerDimension / (max - me.min);
            var pixel = (me.bottom - me.paddingBottom) - (range * (value - me.min));
            return Math.round(pixel);
        }

        return yScale.getPixelForValue(value);
    }
});

Chart.Controller.prototype.draw = function(ease) {
    var me = this;
    var easingDecimal = ease || 1;
    me.clear();

    Chart.plugins.notify('beforeDraw', [me, easingDecimal]);

    // Draw all the scales
    Chart.helpers.each(me.boxes, function(box) {
        box.draw(me.chartArea);
    }, me);
    if (me.scale) {
        me.scale.draw();
    }

    Chart.plugins.notify('beforeDatasetsDraw', [me, easingDecimal]);

    // Draw each dataset via its respective controller (reversed to support proper line stacking)
    Chart.helpers.each(me.data.datasets, function(dataset, datasetIndex) {
        if (me.isDatasetVisible(datasetIndex)) {
            me.getDatasetMeta(datasetIndex).controller.draw(ease);
        }
    }, me, this.options._reverseDrawOrder);

    Chart.plugins.notify('afterDatasetsDraw', [me, easingDecimal]);

    // Finally draw the tooltip
    me.tooltip.transition(easingDecimal).draw();

    Chart.plugins.notify('afterDraw', [me, easingDecimal]);
};


function rightpad(s, size) {
    while (s.length < size)
        s += ' ';
    return s;
}
function leftpad(s, size) {
    while (s.length < size)
        s = ' ' + s;
    return s;
}


function chartForCompetition(element, competition, units) {
  var chartData = {
    type: 'myBar',
    data: {
      groups: [],
      labels: [],
      datasets: [],
    },
    options: {
      _reverseDrawOrder: units.reverseDrawOrder,
      title: {},
      // maintainAspectRatio: false, 
      // responsive: false,
      animation: {
        duration: 0,
      },
      legend: {
        display: false,
        position: 'left',
      },
      tooltips: {
        units: units.label,
        mode: "label",
        titleFontFamily: "'Roboto Condensed', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
        titleFontSize: 14,
        titleFontStyle: 'bold',
        bodyFontFamily: "'Inconsolata', monospace",
        bodyFontSize: 14,
        bodySpacing: 4,
        backgroundColor: 'rgba(0,0,0,0.9)',
        titleMarginBottom: 10,
        xPadding: 10,
        yPadding: 10,
        callbacks: {
          title: function(tooltipItems, data) {
            var chart = this._chartInstance.options.title.text;
            var title = Chart.defaults.global.tooltips.callbacks.title(tooltipItems, data);
            if (competition.preposition) {
              chart += competition.preposition;
            }
            return chart + " " + title;
          },
          label: function(item, data) {
            var chart = this._chartInstance;
            var first;
            for (var i = 0; i < data.datasets.length; i++) {
              if ( ! chart.isDatasetVisible(i)) {
                continue;
              }
              first = data.datasets[i].data[item.index];
              if (first === null) {
                continue;
              }
              break;
            }
            
            var l = data.datasets[item.datasetIndex].label || '';
            var label = " " + rightpad(l, 28);
            var unitsLabel = chart.options.tooltips.units;
            var value = item.yLabel.toFixed(units.valuePrecision);
            var howFaster = units.howFaster(item.yLabel, first);
            if (item.yLabel) {
              label += leftpad('' + value, units.leftpad) + ' ' + unitsLabel;
              if (item.yLabel != first) {
                label += '  ' + howFaster.toFixed(2) + 'x faster';
              }
            }
            return label;
          }
        }
      },
      scales: {
        yAxes: [{
          display: false,
          gridLines: {display: false},
          ticks: {beginAtZero: true},
        }],
        xAxes: [{
          ticks: {
            fontSize: 14,
          },
          gridLines: {display: false},
        }],
      }
    }
  };

  chartData.options.title.text = competition.title;

  var resultsLen = competition.columns.length;

  if (competition.competitors.length) {
    var competitor = competition.competitors[0];
    var lastGroup = null;

    for (var j = 0; j < competitor.results.length; j++) {
      var result = competitor.results[j];
      var group = result.slice(0, -2).join("/");

      if (result.length != resultsLen) {
        throw new Error("results length for " +
                        competitor.title + " doesn't match required. " +
                        "Got " + result.length + ", expected " + resultsLen);
      }

      var label = [];
      for (var k = 0; k < result.length - 1; k++) {
        if (competition.columns[k]['map']) {
          label.push(competition.columns[k]['map'][result[k]])
        } else {
          label.push(result[k])
        }
      }

      if (lastGroup && group != lastGroup) {
        chartData.data.labels.push("");
        if (group) {
          chartData.data.groups.push("");
        }
      }
      lastGroup = group;

      chartData.data.labels.push(label.join(" "));
      if (group) {
        chartData.data.groups.push(group);
      }
    }
  }

  for (var i = 0; i < competition.competitors.length; i++) {
    var competitor = competition.competitors[i];
    var color = competitor.color;
    var data = [];
    var lastGroup = null;

    if (typeof color != "string") {
      color = "hsla("+color[0]+","+color[1]+"%,"+color[2]+"%,1.0)";
    }

    chartData.data.datasets.push({
      label: competitor.title,
      name: competitor.name,
      data: data,
      backgroundColor: color,
      borderColor: "rgba(255, 255, 255, .5)",
      borderWidth: 1,
    });

    for (var j = 0; j < competitor.results.length; j++) {
      var result = competitor.results[j];
      var group = result.slice(0, -2).join("/");

      if (lastGroup && group != lastGroup) {
        data.push(null);
      }
      lastGroup = group;

      data.push(units.formatValue(result[result.length - 1], competition));
    }
  }

  return new Chart(element, chartData);
}


function applyPreset(chart, presetArr) {
  var preset = {};
  for (var i = 0; i < presetArr.length; i++) {
    preset[presetArr[i]] = true;
  }

  for (var i = 0; i < chart.data.datasets.length; i++) {
    var meta = chart.getDatasetMeta(i);
    var dataset = chart.data.datasets[i];

    meta.hidden = ! preset[dataset.name];
  }

  chart.update();
}


module.exports = {
  Chart: Chart,
  chartForCompetition: chartForCompetition,
  applyPreset: applyPreset,
};
