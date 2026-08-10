import os
import logging
import asyncio
import threading
from flask import Flask, jsonify

# Импортируем функцию main() из вашего bot.py
from bot import main as bot_main

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def root():
    return "✅ Бот работает!", 200

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

# --- Функция для запуска бота в отдельном потоке с собственным циклом ---
def run_bot():
    """Создает новый event loop и запускает в нем основную функцию бота."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(bot_main())
    except Exception as e:
        logger.exception(f"Критическая ошибка в потоке бота: {e}")
    finally:
        loop.close()

if __name__ == '__main__':
    # 1. Запускаем бота в фоновом потоке
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    logger.info("✅ Бот запущен в фоновом потоке")

    # 2. Запускаем Flask-сервер в главном потоке
    port = int(os.getenv('PORT', 10000))
    logger.info(f"🚀 Запуск Flask-сервера на порту {port}")
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
