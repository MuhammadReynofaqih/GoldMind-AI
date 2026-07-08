import pandas as pd


class MarketStructure:

    def __init__(self, df):
        self.df = df.copy()

    def swing_highs(self, left=3, right=3):

        swings = []

        for i in range(left, len(self.df)-right):

            if self.df["high"].iloc[i] == max(
                self.df["high"].iloc[i-left:i+right+1]
            ):
                swings.append(i)

        return swings

    def swing_lows(self, left=3, right=3):

        swings = []

        for i in range(left, len(self.df)-right):

            if self.df["low"].iloc[i] == min(
                self.df["low"].iloc[i-left:i+right+1]
            ):
                swings.append(i)

        return swings

    def bos(self):

        highs = self.swing_highs()

        if len(highs) < 2:
            return "UNKNOWN"

        last = highs[-1]
        prev = highs[-2]

        if self.df["high"].iloc[last] > self.df["high"].iloc[prev]:
            return "BULLISH BOS"

        return "BEARISH BOS"

    def choch(self):

        lows = self.swing_lows()

        if len(lows) < 2:
            return "UNKNOWN"

        last = lows[-1]
        prev = lows[-2]

        if self.df["low"].iloc[last] < self.df["low"].iloc[prev]:
            return "BEARISH CHOCH"

        return "BULLISH CHOCH"

    def trend(self):

        close = self.df["close"]

        ema20 = close.rolling(20).mean()

        ema50 = close.rolling(50).mean()

        if ema20.iloc[-1] > ema50.iloc[-1]:
            return "BULLISH"

        return "BEARISH"

    def analyze(self):

        return {

            "Trend": self.trend(),

            "BOS": self.bos(),

            "CHOCH": self.choch()

        }