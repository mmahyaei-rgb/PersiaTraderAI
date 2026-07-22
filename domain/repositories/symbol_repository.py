from abc import ABC, abstractmethod


class SymbolRepository(ABC):

    @abstractmethod
    def add(self, symbol):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def find(self, symbol):
        pass
    