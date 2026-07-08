class FVGEngine:

    def __init__(self, df):
        self.df = df

    def bullish(self):

        gaps = []

        for i in range(2, len(self.df)):

            c1 = self.df.iloc[i-2]
            c3 = self.df.iloc[i]

            if c1["high"] < c3["low"]:

                gaps.append({

                    "type": "Bullish",

                    "top": c3["low"],

                    "bottom": c1["high"],

                    "index": i

                })

        return gaps

    def bearish(self):

        gaps = []

        for i in range(2, len(self.df)):

            c1 = self.df.iloc[i-2]
            c3 = self.df.iloc[i]

            if c1["low"] > c3["high"]:

                gaps.append({

                    "type": "Bearish",

                    "top": c1["low"],

                    "bottom": c3["high"],

                    "index": i

                })

        return gaps