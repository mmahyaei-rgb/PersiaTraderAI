from strategies.ema_strategy import EmaStrategy
from strategies.rsi_strategy import RsiStrategy


class StrategyEngine:

    def __init__(self):

        self.strategies = [

            EmaStrategy(),

            RsiStrategy()

        ]

    def analyze(self, df):

        results = []

        for strategy in self.strategies:

            results.append(strategy.analyze(df))

        return results
    