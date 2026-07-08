import MetaTrader5 as mt5

from data.market_data import *

from engine.market_structure_engine import MarketStructure

initialize()

df = get_rates(

    "XAUUSDc",

    mt5.TIMEFRAME_H1,

    500

)

engine = MarketStructure(df)

result = engine.analyze()

print()

for k, v in result.items():

    print(k, ":", v)

shutdown()