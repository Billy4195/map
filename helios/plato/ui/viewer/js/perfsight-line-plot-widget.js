
class PerfSightLinePlotWidget extends SimpleLinePlotWidget {
    constructor(el, id) {
        super(el, id)

        // Initial values
        this._stat_cols = []
    }
}
PerfSightLinePlotWidget.typename = 'perfsight-line-plot'
PerfSightLinePlotWidget.description = 'A simple line plot from perfsight CSV file'
PerfSightLinePlotWidget.processor_type = Processors.PERFSIGHT
PerfSightLinePlotWidget.data_type = DataTypes.PERFSIGHT_LINE
