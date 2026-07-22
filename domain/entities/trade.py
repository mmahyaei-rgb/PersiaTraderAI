from dataclasses import dataclass


@dataclass
class Trade:

    symbol: str

    entry_price: float

    exit_price: float

    quantity: int

    profit: float

    signal: str
    