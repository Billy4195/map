from plato.backend.units import Units

from plato.backend.datasources.perfsight.datasource import PerfSightDataSource
from ..general_trace.adapter import GeneralTraceAdapter


# Example adapter for a random pseudo-data-source
class PerfSightAdapter(GeneralTraceAdapter):

    statsForUnits = {Units.CYCLES: PerfSightDataSource.cyclesStat}

    def __init__(self, data_source: PerfSightDataSource):
        super().__init__(data_source)

    # Override: We know this trace has trn_idx and cycles columns
    def get_stat_for_units(self, units):
        if units in PerfSightAdapter.statsForUnits:
            return PerfSightAdapter.statsForUnits[units]

        return super().get_stat_for_units(units)
