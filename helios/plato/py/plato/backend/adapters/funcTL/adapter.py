
class FuncTLAdapter:
    def __init__(self, data_source):
        self.data_source = data_source
        self.pdf = self.data_source.pdf()
        self.pdf['func'] = self.pdf['func'].fillna('')
        self.pdf['rtnAddr'] = self.pdf['rtnAddr'].fillna('')

    def get_grids(self, first, last):
        filtered_pdf = self.pdf[~((self.pdf['endCycle'] < first) & (self.pdf['startCycle'] > last))]
        filtered_pdf = filtered_pdf[['func', 'startCycle', 'endCycle', 'callDepth']]

        return filtered_pdf.to_numpy().tolist()
