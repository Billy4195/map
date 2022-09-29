from logging import info, debug
import time

import numpy as np
import pandas as pd
from plato.backend.units import Units

class FuncTLDataSource:
    def __init__(self, filename):
        start_ts = time.time()
        self._pdf = pd.read_csv(filename)

        info("spent {}ms building dataframe".format((time.time() - start_ts) * 1000))

    @staticmethod
    def get_source_information(filename: str):
        df = pd.read_csv(filename)
        
        return {'timeRange': [{'units': Units.CYCLES,
                               'first': int(df['startCycle'].min()),
                               'last': int(df['endCycle'].max())}],
                'typeSpecific': {'startCycle': df['startCycle'].astype(int).to_list()},
                'stats': []
            }


    def pdf(self):
        return self._pdf
