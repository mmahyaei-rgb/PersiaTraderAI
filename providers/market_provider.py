import pandas as pd

from providers.tsetmc_client import TSETMCClient


class MarketProvider:

    def __init__(self):

        self.client = TSETMCClient()

    def get_market_watch(self):

        # فعلاً فقط تست اتصال
        data = self.client.get("StaticData/GetTime")

        print(data)

        return pd.DataFrame()
    