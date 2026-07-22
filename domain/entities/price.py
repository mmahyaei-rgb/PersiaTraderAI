from dataclasses import dataclass


@dataclass
class Price:

    symbol: str

    date: str

    open: float

    high: float

    low: float

    close: float

    volume: float

    value: float
    