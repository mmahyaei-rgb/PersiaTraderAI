from application.market.market_engine import MarketEngine
from analysis.scanner import Scanner

engine = MarketEngine()

df = engine.update()

signals = Scanner.scan(df)

print()

print("===== PersiaTraderAI =====")

for signal in signals:

    print(signal.value)

from backtest.backtester import BackTester

bt = BackTester()

bt.add_trade(

    "FOLD",

    1500,

    1580,

    100,

    "BUY"

)

bt.add_trade(

    "FOLD",

    1580,

    1550,

    100,

    "SELL"

)

print()

print(bt.report())
    