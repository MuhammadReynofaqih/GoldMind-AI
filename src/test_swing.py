import MetaTrader5 as mt5

from data.market_data import *
from engine.swing_engine import SwingEngine

initialize()

df = get_rates(
    "XAUUSDc",
    mt5.TIMEFRAME_H1,
    300
)

engine = SwingEngine()

highs, lows = engine.detect(df)

print()

print("Swing High")

for h in highs[-10:]:

    print(df.iloc[h]["time"], df.iloc[h]["high"])

print()

print("Swing Low")

for l in lows[-10:]:

    print(df.iloc[l]["time"], df.iloc[l]["low"])

shutdown()