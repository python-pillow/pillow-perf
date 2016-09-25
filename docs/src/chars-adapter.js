var Chart = require("chart.js/dist/Chart.js");

module.exports = Chart;

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

        if (me.chart.data.groups) {
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
    }, me);

    Chart.plugins.notify('afterDatasetsDraw', [me, easingDecimal]);

    // Finally draw the tooltip
    me.tooltip.transition(easingDecimal).draw();

    Chart.plugins.notify('afterDraw', [me, easingDecimal]);
};
