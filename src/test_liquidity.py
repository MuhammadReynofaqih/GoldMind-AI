import MetaTrader5 as mt5

from data.market_data import *

from engine.liquidity_engine import LiquidityEngine

initialize()

df = get_rates("XAUUSDc", mt5.TIMEFRAME_H1, 200)

engine = LiquidityEngine(df)

eqh = engine.equal_high()

eql = engine.equal_low()

print()

print("Equal High :", len(eqh))

print("Equal Low :", len(eql))

shutdown()