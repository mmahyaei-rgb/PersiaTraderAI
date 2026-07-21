from analysis.indicators import Indicators


class Scanner:

    def analyse(self, df):

        df["EMA20"] = Indicators.ema(df["close"],20)

        df["EMA50"] = Indicators.ema(df["close"],50)

        df["RSI"] = Indicators.rsi(df["close"])

        return df
    