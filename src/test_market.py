from data.market_data import *

initialize()

df = get_rates()

print(df.tail())

shutdown()