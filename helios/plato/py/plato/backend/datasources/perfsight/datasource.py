from logging import info, debug
import sqlite3
import time

import numpy as np
import pandas as pd
from plato.backend.units import Units


class PerfSightDataSource:
    '''
    this will read the csv files generated from perfsight cli
    '''
    cyclesStat = 'cycle'
    def __init__(self, filename):
        start = int(round(time.time() * 1000))
        self._pdf = pd.read_csv(filename)
        if 'cycle' in self._pdf:
            val_cols = self._pdf.columns.drop("cycle")
            self._pdf[val_cols] = self._pdf[val_cols].diff().fillna(self._pdf[val_cols].iloc[0]) # use diff() because counters are accumulated

        info("spent {}ms building dataframe".format((time.time() - start)) * 1000)

    @staticmethod
    def get_source_information(filename: str):
        '''
        go grab basic stats from this sqlite file
        '''
        df = pd.read_csv(filename)
        if 'cycle' in df:
            time_units = df['cycle']
        nodeList = []
        for statName in df.columns:
            if statName != 'cycle':
                nodeList.append(statName)

        return {'timeRange': [{'units': Units.CYCLES,
                               'first': int(time_units.min()),  # numpy.int64 -> int (due to JSON)
                               'last': int(time_units.max())}],
                'typeSpecific': {'statCount': len(nodeList),
                                 'startCycle': time_units.astype(int).to_list()},
                'stats': nodeList
                }

    @property
    def stats(self):
        return self._pdf.columns

    # Overriding GeneralTraceDataSource to give GeneralTraceAdapter adapter access to raw data
    def pdf(self) -> pd.DataFrame:
        return self._pdf
