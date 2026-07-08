import pandas as pd


class SwingEngine:

    def detect(self, df, left=3, right=3):

        highs = []
        lows = []

        for i in range(left, len(df) - right):

            high = df["high"].iloc[i]

            if high == max(df["high"].iloc[i-left:i+right+1]):
                highs.append(i)

            low = df["low"].iloc[i]

            if low == min(df["low"].iloc[i-left:i+right+1]):
                lows.append(i)

        return highs, lows