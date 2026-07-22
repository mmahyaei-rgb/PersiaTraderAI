from database.database import Database


class MarketRepository:

    def __init__(self):

        self.db = Database()

    def save_symbol(self, symbol, name):

        self.db.insert_symbol(symbol, name)

    def save_price(self, row):

        self.db.insert_price(
            symbol=row["symbol"],
            date=row["date"],
            open_price=row["open"],
            high=row["high"],
            low=row["low"],
            close=row["close"],
            volume=row["volume"],
            value=row["value"],
        )

    def close(self):

        self.db.close()
        