from providers.market_provider import MarketProvider

from analysis.scanner import Scanner

provider = MarketProvider()

scanner = Scanner()

df = provider.load_demo()

result = scanner.analyse(df)

print(result.tail())
