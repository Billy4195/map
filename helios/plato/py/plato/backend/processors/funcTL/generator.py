

class FuncTLGenerator:
    def __init__(self, adapter):
        self._adapter = adapter
    

    def generate_grids(self, first, last):
        grids = self._adapter.get_grids(first, last)

        return grids
