from analysis.moving_average import MovingAverage


class IndicatorEngine:

    @staticmethod
    def calculate(df):

        df["SMA20"] = MovingAverage.sma(df["close"], 20)

        df["EMA20"] = MovingAverage.ema(df["close"], 20)

        return df
    