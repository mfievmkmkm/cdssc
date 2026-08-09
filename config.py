import os
from dotenv import load_dotenv

load_dotenv()

# --- ОСНОВНЫЕ НАСТРОЙКИ ---
TOKEN = os.getenv("TOKEN")
ADMIN = int(os.getenv("ADMIN", 0))

PRIVATE_CHANNEL_ID = os.getenv("PRIVATE_CHANNEL_ID")
PRIVATE_CHAT_ID = os.getenv("PRIVATE_CHAT_ID")

# --- ПОДКЛЮЧЕНИЕ К БД (POSTGRESQL) ---
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")  # Добавьте эту переменную в Railway

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# --- ЦЕНЫ ТАРИФОВ (Telegram Stars) ---
PRICES = {
    "month": 1,
    "sixmonth": 500,
    "year": 900
}
