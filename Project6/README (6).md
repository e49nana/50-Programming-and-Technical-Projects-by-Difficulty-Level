# 🌤️ Weather Telegram Bot

A Telegram bot that replies with the current weather for any city using OpenWeatherMap API.

## ✅ Features
- Replies to any city name with live temperature and weather description
- Uses OpenWeatherMap API
- Lightweight and easy to deploy

## ▶️ Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up your `.env` file
Rename `.env.example` to `.env` and add your credentials:
```
TELEGRAM_TOKEN=your_bot_token
WEATHER_API_KEY=your_openweathermap_api_key
```

### 3. Run the bot
```bash
python weather_bot.py
```

## 🧠 How it works
- The user sends a city name
- The bot fetches weather data via OpenWeatherMap API
- The bot replies with current temperature and sky description

---

Made for learning and practical API integration.
