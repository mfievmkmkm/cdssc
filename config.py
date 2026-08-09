import os
import pytz
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = os.getenv('TOKEN')
OWNER_ID = int(os.getenv('ADMIN', 0))
CHANNEL_ID = int(os.getenv('PRIVATE_CHANNEL_ID', 0))
CHAT_ID = int(os.getenv('PRIVATE_CHAT_ID', 0))

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@postgres_db:5432/{DB_NAME}'

MSK = pytz.timezone('Europe/Moscow')
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())