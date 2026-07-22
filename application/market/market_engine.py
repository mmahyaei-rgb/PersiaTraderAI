from infrastructure.providers.provider_manager import ProviderManager


class MarketEngine:

    def __init__(self):

        self.provider = ProviderManager()

    def update(self):

        return self.provider.market()
    