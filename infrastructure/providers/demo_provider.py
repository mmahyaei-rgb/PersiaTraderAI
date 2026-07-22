import pandas as pd
import random

from infrastructure.providers.base_provider import BaseProvider


class DemoProvider(BaseProvider):

    def get_market_watch(self):

        price = 1000

        rows = []

        for i in range(200):

            price += random.randint(-15, 20)

            rows.append(
                {
                    "symbol": "FOLD",
                    "name": "فولاد مبارکه",
                    "close": price,
                    "volume": random.randint(100000, 500000),
                    "value": random.randint(100000000, 500000000)
                }
            )

        return pd.DataFrame(rows)
    