import MetaTrader5 as mt5

from data.market_data import *
from smc.pivot import Pivot

initialize()

df = get_rates(
    "XAUUSDc",
    mt5.TIMEFRAME_H1,
    500
)

pivot = Pivot(df)

highs = pivot.highs()

lows = pivot.lows()

print()

print("Swing High :", len(highs))

print("Swing Low :", len(lows))

print()

print(highs[-5:])

print()

print(lows[-5:])

shutdown()