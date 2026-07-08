import MetaTrader5 as mt5
import pandas as pd


class MarketData:

    def __init__(self):
        if not mt5.initialize():
            raise Exception(mt5.last_error())

    def get_rates(self, symbol, timeframe, bars=500):
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)

        if rates is None:
            return None

        df = pd.DataFrame(rates)

        df["time"] = pd.to_datetime(df["time"], unit="s")

        return df

    def shutdown(self):
        mt5.shutdown()