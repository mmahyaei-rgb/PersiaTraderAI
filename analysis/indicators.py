import pandas as pd


class Indicators:

    @staticmethod
    def sma(series, period):

        return series.rolling(period).mean()

    @staticmethod
    def ema(series, period):

        return series.ewm(span=period).mean()

    @staticmethod
    def rsi(series, period=14):

        delta = series.diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(period).mean()

        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))
    