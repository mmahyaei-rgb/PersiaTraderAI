import sqlite3
from config import DATABASE_FILE


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS symbols(
            symbol TEXT PRIMARY KEY,
            name TEXT,
            market TEXT,
            industry TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_prices(
            symbol TEXT,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL,
            value REAL,
            PRIMARY KEY(symbol, date)
        )
        """)

        self.conn.commit()

    def insert_symbol(self, symbol, name, market="", industry=""):

        self.cursor.execute("""
        INSERT OR REPLACE INTO symbols
        (symbol, name, market, industry)
        VALUES (?, ?, ?, ?)
        """, (symbol, name, market, industry))

        self.conn.commit()

    def get_symbols(self):

        self.cursor.execute("SELECT * FROM symbols")

        return self.cursor.fetchall()

    def insert_price(
        self,
        symbol,
        date,
        open_price,
        high,
        low,
        close,
        volume,
        value
    ):

        self.cursor.execute("""
        INSERT OR REPLACE INTO daily_prices
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            symbol,
            date,
            open_price,
            high,
            low,
            close,
            volume,
            value
        ))

        self.conn.commit()

    def close(self):
        self.conn.close()
        