import MetaTrader5 as mt5

from data.market_data import *
from engine.order_block_engine import OrderBlockEngine

initialize()

df = get_rates(
    "XAUUSDc",
    mt5.TIMEFRAME_H1,
    300
)

engine = OrderBlockEngine(df)

print()

print(engine.bullish())

print()

print(engine.bearish())

shutdown()