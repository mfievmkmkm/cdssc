FROM python:3.13-slim

WORKDIR /app

# Устанавливаем системные зависимости для asyncpg (PostgreSQL)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем и устанавливаем Python-зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запускаем бота (используйте правильный файл входа)
CMD ["python", "bot.py"]
