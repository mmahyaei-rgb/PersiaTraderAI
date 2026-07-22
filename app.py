from application.market.market_engine import MarketEngine

engine = MarketEngine()

df = engine.update()

print(df[[
    "close",
    "SMA20",
    "EMA20",
    "RSI14"
]].tail())
