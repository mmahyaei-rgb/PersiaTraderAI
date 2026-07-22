from analysis.signal import Signal
from strategies.base_strategy import BaseStrategy


class EmaStrategy(BaseStrategy):

    def analyze(self, df):

        last = df.iloc[-1]

        if last["EMA20"] > last["SMA20"]:

            return Signal.BUY

        return Signal.HOLD
    