from dataclasses import dataclass


@dataclass
class Candle:

    symbol: str

    date: str

    open: float

    high: float

    low: float

    close: float

    volume: float

    value: float
    