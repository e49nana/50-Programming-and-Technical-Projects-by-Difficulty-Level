import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌍 Send me a city name to get the current weather!")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text.strip()
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "en"
    }
    try:
        res = requests.get(WEATHER_URL, params=params)
        data = res.json()
        if res.status_code == 200:
            description = data['weather'][0]['description'].capitalize()
            temp = data['main']['temp']
            await update.message.reply_text(f"📍 {city}\n🌡️ {temp}°C, {description}")
        else:
            await update.message.reply_text("⚠️ City not found.")
    except Exception as e:
        await update.message.reply_text("❌ Error retrieving weather data.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, weather))
    print("Bot running...")
    app.run_polling()
