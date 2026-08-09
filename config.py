import os
import pytz
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = os.getenv('TOKEN')
OWNER_ID = int(os.getenv('ADMIN', 0))
CHANNEL_ID = int(os.getenv('PRIVATE_CHANNEL_ID', 0))
CHAT_ID = int(os.getenv('PRIVATE_CHAT_ID', 0))

# SQLite вместо PostgreSQL
DATABASE_URL = 'sqlite:///gift_bot.db'

MSK = pytz.timezone('Europe/Moscow')
print(f"TOKEN = {TOKEN}")
print(f"DATABASE_URL = {DATABASE_URL}")
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())