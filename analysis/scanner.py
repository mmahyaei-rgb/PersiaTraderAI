from strategies.strategy_engine import StrategyEngine


class Scanner:

    @staticmethod
    def scan(df):

        engine = StrategyEngine()

        signals = engine.analyze(df)

        return signals
    