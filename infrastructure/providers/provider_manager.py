from infrastructure.providers.demo_provider import DemoProvider


class ProviderManager:

    def __init__(self):

        self.provider = DemoProvider()

    def market(self):

        return self.provider.get_market_watch()
    