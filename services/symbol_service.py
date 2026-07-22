from database.database import Database


class SymbolService:

    def __init__(self):

        self.db = Database()

    def add_symbol(self, symbol, name):

        self.db.insert_symbol(symbol, name)

    def all(self):

        return self.db.get_symbols()
    