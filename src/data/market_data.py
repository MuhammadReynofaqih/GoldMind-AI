import MetaTrader5 as mt5
import pandas as pd


def initialize():

    if not mt5.initialize():
        raise Exception(mt5.last_error())


def shutdown():
    mt5.shutdown()


def get_rates(symbol="XAUUSDc", timeframe=mt5.TIMEFRAME_H1, bars=200):

    rates = mt5.copy_rates_from_pos(
        symbol,
        timeframe,
        0,
        bars
    )

    df = pd.DataFrame(rates)

    df["time"] = pd.to_datetime(
        df["time"],
        unit="s"
    )

    return df