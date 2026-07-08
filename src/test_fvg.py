import MetaTrader5 as mt5

from data.market_data import *
from engine.fvg_engine import FVGEngine

initialize()

df = get_rates(
    "XAUUSDc",
    mt5.TIMEFRAME_H1,
    300
)

engine = FVGEngine(df)

print()

print("Bullish FVG :", len(engine.bullish()))

print("Bearish FVG :", len(engine.bearish()))

shutdown()