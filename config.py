from pathlib import Path

BASE_DIR = Path(__file__).parent

DATABASE_FILE = BASE_DIR / "data" / "market.db"

LOG_FILE = BASE_DIR / "logs" / "persia_trader.log"
