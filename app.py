from application.market.market_engine import MarketEngine


engine = MarketEngine()

data = engine.update()

print(data)
