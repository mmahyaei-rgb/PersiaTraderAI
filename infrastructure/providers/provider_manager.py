from infrastructure.providers.demo_provider import DemoProvider
from infrastructure.providers.csv_provider import CSVProvider


class ProviderManager:

    def __init__(self):

        self.provider = DemoProvider()

    def use_demo(self):

        self.provider = DemoProvider()

    def use_csv(self, path):

        self.provider = CSVProvider(path)

    def market(self):

        return self.provider.get_market_watch()
    