from dataclasses import dataclass
from datetime import datetime


@dataclass
class Candle:
    time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    @property
    def bullish(self):
        return self.close > self.open

    @property
    def bearish(self):
        return self.close < self.open

    @property
    def body(self):
        return abs(self.close - self.open)

    @property
    def range(self):
        return self.high - self.low