import os
from pathlib import Path

from config.env import get_env

BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE: str = os.getenv("ENV_FILE", ".env")
ENV = get_env(env_file=BASE_DIR / ENV_FILE)

BOT_TOKEN = ENV.str("BOT_TOKEN")
DEBUG = ENV.bool("DEBUG", False)

LOGS_FOLDER = ENV.str("LOGS_FOLDER", "logs")
LOGS_DIR = BASE_DIR / LOGS_FOLDER

POSTGRES_URL = ENV.str("POSTGRES_URL")
REDIS_URL = ENV.str("REDIS_URL")

GOOGLE_API_KEY = ENV.str("GOOGLE_API_KEY")
GOOGLE_TABLE_ID = ENV.str("GOOGLE_TABLE_ID")

COMPETITION_SHEET_NAME_RE = r"---.*---"
