class OrderBlockEngine:

    def __init__(self, df):
        self.df = df

    def bullish(self):

        for i in range(len(self.df)-2, 20, -1):

            c1 = self.df.iloc[i]
            c2 = self.df.iloc[i+1]

            if (
                c1["close"] < c1["open"]
                and c2["close"] > c1["high"]
            ):

                return {
                    "type": "Bullish",
                    "index": i,
                    "high": c1["high"],
                    "low": c1["low"]
                }

        return None

    def bearish(self):

        for i in range(len(self.df)-2, 20, -1):

            c1 = self.df.iloc[i]
            c2 = self.df.iloc[i+1]

            if (
                c1["close"] > c1["open"]
                and c2["close"] < c1["low"]
            ):

                return {
                    "type": "Bearish",
                    "index": i,
                    "high": c1["high"],
                    "low": c1["low"]
                }

        return None