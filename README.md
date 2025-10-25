# Telegram OpenAI Bot

Бот для генерации текста и изображений через OpenAI API.

## 🚀 Как запустить

1. Создай файл `.env` и вставь свои ключи:  
   ```
   TELEGRAM_BOT_TOKEN=...
   OPENAI_API_KEY=...
   ```

2. Установи зависимости:  
   ```
   pip install -r requirements.txt
   ```

3. Запусти бота:  
   ```
   python bot.py
   ```

## 🧐 Команды

- `/start` — приветствие  
- `/text <запрос>` — сгенерировать текст  
- `/image <описание>` — создать изображение 
