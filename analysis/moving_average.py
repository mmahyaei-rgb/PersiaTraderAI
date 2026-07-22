import pandas as pd


class MovingAverage:

    @staticmethod
    def sma(data: pd.Series, period: int):

        return data.rolling(period).mean()

    @staticmethod
    def ema(data: pd.Series, period: int):

        return data.ewm(span=period, adjust=False).mean()
    