import MetaTrader5 as mt5

from data.market_data import *
from engine.swing_engine import SwingEngine
from engine.bos_engine import BOSEngine

initialize()

df = get_rates(
    "XAUUSDc",
    mt5.TIMEFRAME_H1,
    300
)

swing = SwingEngine()

highs, lows = swing.detect(df)

bos = BOSEngine()

print()

print(bos.detect(df, highs, lows))

shutdown()