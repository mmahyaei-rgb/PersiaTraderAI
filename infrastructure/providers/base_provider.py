from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def get_market_watch(self):
        """
        باید اطلاعات بازار را به صورت pandas.DataFrame برگرداند.
        """
        pass
    