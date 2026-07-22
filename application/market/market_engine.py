from infrastructure.providers.provider_manager import ProviderManager
from analysis.indicator_engine import IndicatorEngine


class MarketEngine:

    def __init__(self):

        self.provider = ProviderManager()

        self.provider.use_csv("data/market/FOLD.csv")

    def update(self):

        df = self.provider.market()

        df = IndicatorEngine.calculate(df)

        return df
    