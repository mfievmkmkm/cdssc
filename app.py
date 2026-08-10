import os
import logging
import threading
from flask import Flask, jsonify
from bot import main as bot_main

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаем Flask приложение
app = Flask(__name__)

@app.route('/')
def root():
    return "✅ Бот работает!", 200

@app.route('/health')
def health():
    return jsonify({"status": "ok", "message": "Bot is running"}), 200

@app.route('/ping')
def ping():
    return "pong", 200

if __name__ == '__main__':
    # Запускаем бота в отдельном потоке, чтобы Flask не блокировал его
    bot_thread = threading.Thread(target=bot_main, daemon=True)
    bot_thread.start()
    logger.info("Бот запущен в фоновом потоке")
    
    # Получаем порт от Render (обязательно!)
    port = int(os.getenv('PORT', 10000))
    logger.info(f"Запуск Flask-сервера на порту {port}")
    
    # Запускаем Flask сервер
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
