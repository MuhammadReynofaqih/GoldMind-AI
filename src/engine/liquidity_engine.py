class LiquidityEngine:

    def __init__(self, df):
        self.df = df

    def equal_high(self, tolerance=0.5):

        highs = self.df["high"].tolist()

        results = []

        for i in range(len(highs)-1):

            for j in range(i+1, len(highs)):

                if abs(highs[i]-highs[j]) <= tolerance:

                    results.append((i, j, highs[i]))

        return results

    def equal_low(self, tolerance=0.5):

        lows = self.df["low"].tolist()

        results = []

        for i in range(len(lows)-1):

            for j in range(i+1, len(lows)):

                if abs(lows[i]-lows[j]) <= tolerance:

                    results.append((i, j, lows[i]))

        return results