from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASE_FILE = BASE_DIR / "data" / "market.db"
LOG_FOLDER = BASE_DIR / "logs"

LOG_FOLDER.mkdir(parents=True, exist_ok=True)
DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)
