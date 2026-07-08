import pandas as pd


class Pivot:

    def __init__(self, df):
        self.df = df

    def highs(self, window=3):

        result = []

        for i in range(window, len(self.df)-window):

            value = self.df.high.iloc[i]

            left = self.df.high.iloc[i-window:i]

            right = self.df.high.iloc[i+1:i+window+1]

            if value > left.max() and value > right.max():

                result.append({
                    "index": i,
                    "price": value,
                    "time": self.df.time.iloc[i]
                })

        return result

    def lows(self, window=3):

        result = []

        for i in range(window, len(self.df)-window):

            value = self.df.low.iloc[i]

            left = self.df.low.iloc[i-window:i]

            right = self.df.low.iloc[i+1:i+window+1]

            if value < left.min() and value < right.min():

                result.append({
                    "index": i,
                    "price": value,
                    "time": self.df.time.iloc[i]
                })

        return result