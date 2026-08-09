import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, Boolean
from datetime import datetime

# --- ПОДКЛЮЧЕНИЕ К POSTGRESQL ---
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")  # Эту переменную нужно добавить на Railway!

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Движок для асинхронной работы с PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=False)

# Фабрика сессий
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

# --- МОДЕЛИ (пример, адаптируйте под свои) ---
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True, nullable=False)
    subscribed_until = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False)
    tariff = Column(String, nullable=False)  # 'month', 'sixmonth', 'year'

# --- СОЗДАНИЕ ТАБЛИЦ ---
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# --- МИДЛВАРЬ ДЛЯ ДОСТУПА К СЕССИИ БД (если используется) ---
class DatabaseMiddleware:
    async def __call__(self, request, call_next):
        async with async_session() as session:
            request.state.db = session
            response = await call_next(request)
            return response
