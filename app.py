from application.market.market_engine import MarketEngine

engine = MarketEngine()

df = engine.update()

print(df.tail())
