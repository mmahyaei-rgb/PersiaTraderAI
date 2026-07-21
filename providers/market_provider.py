import pandas as pd


class MarketProvider:

    def load_demo(self):

        close = [

            100,102,103,101,104,

            106,107,109,108,111,

            112,114,116,118,119,

            120,121,123,124,125,

            126,127,129,130,132,

            133,135,136,138,140

        ]

        return pd.DataFrame({

            "close":close

        })
        