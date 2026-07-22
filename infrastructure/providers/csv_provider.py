import pandas as pd


class CSVProvider:

    def __init__(self, path):

        self.path = path

    def get_market_watch(self):

        return pd.read_csv(self.path)
    