from analysis.moving_average import MovingAverage
from analysis.rsi import RSI


class IndicatorEngine:

    @staticmethod
    def calculate(df):

        df["SMA20"] = MovingAverage.sma(df["close"], 20)
        df["EMA20"] = MovingAverage.ema(df["close"], 20)
        df["RSI14"] = RSI.calculate(df["close"], 14)

        return df
    