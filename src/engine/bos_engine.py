class BOSEngine:

    def detect(self, df, highs, lows):

        if len(highs) < 2:
            return "UNKNOWN"

        last = highs[-1]
        prev = highs[-2]

        if df["high"].iloc[last] > df["high"].iloc[prev]:
            return "BULLISH BOS"

        return "BEARISH BOS"