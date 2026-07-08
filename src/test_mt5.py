import MetaTrader5 as mt5

if not mt5.initialize():
    print("Failed to connect MT5")
    print(mt5.last_error())
else:
    print("Connected to MT5")
    print(mt5.version())
    mt5.shutdown()