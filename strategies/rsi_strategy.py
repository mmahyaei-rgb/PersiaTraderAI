from analysis.signal import Signal
from strategies.base_strategy import BaseStrategy


class RsiStrategy(BaseStrategy):

    def analyze(self, df):

        last = df.iloc[-1]

        if last["RSI14"] < 30:

            return Signal.BUY

        if last["RSI14"] > 70:

            return Signal.SELL

        return Signal.HOLD
    