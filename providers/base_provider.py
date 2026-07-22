from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def get_market_watch(self):
        pass
    