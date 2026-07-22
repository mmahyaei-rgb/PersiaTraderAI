from dataclasses import dataclass


@dataclass
class Symbol:

    symbol: str

    name: str

    market: str = ""

    industry: str = ""
    