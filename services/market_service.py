from providers.market_provider import MarketProvider
from database.database import Database
from utils.date_utils import today
from logger import logger


class MarketService:

    def __init__(self):
        self.provider = MarketProvider()
        self.db = Database()

    def sync_market(self):

        try:

            print("شروع بروزرسانی بازار ...")

            df = self.provider.get_market_watch()

            for _, row in df.iterrows():

                self.db.insert_symbol(
                    row["symbol"],
                    row["name"]
                )

                self.db.insert_price(
                    symbol=row["symbol"],
                    date=today(),
                    open_price=row["close"],
                    high=row["close"],
                    low=row["close"],
                    close=row["close"],
                    volume=row["volume"],
                    value=row["value"]
                )

            print(f"{len(df)} رکورد ذخیره شد.")
            logger.info("Market Updated Successfully")

        except Exception as e:

            logger.exception(e)
            print(e)

        finally:

            self.db.close()
            