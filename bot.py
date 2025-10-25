import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from openai_client import generate_text, generate_image

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот с OpenAI. Используй /text или /image ✨")

async def text_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("❗ Напиши запрос после команды /text")
        return
    await update.message.reply_text("Генерирую ответ... ⏳")
    result = await generate_text(prompt)
    await update.message.reply_text(result)

async def image_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("❗ Напиши описание после команды /image")
        return
    await update.message.reply_text("Создаю изображение... 🎨")
    image_url = await generate_image(prompt)
    await update.message.reply_photo(image_url)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("text", text_command))
    app.add_handler(CommandHandler("image", image_command))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
