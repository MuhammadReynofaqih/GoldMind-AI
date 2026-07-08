import MetaTrader5 as mt5
from data.market_data import MarketData

md = MarketData()

df = md.get_rates(
    "XAUUSDc",
    mt5.TIMEFRAME_H1,
    20
)

print(df)

md.shutdown()