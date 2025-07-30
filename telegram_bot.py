from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from services.weather_api import WeatherFetcher
from services.location_service import LocationService

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌤️ Hava Durumu Botuna Hoş Geldiniz!\n"
        "Komutlar:\n"
        "/weather <konum> - Hava durumu bilgisi\n"
        "/compare <konum> - 3 kaynaktan karşılaştırma"
    )

async def get_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = " ".join(context.args)
    lat, lon = LocationService.get_coordinates(location)
    
    weather_data = WeatherFetcher.get_openweather(lat, lon)
    temp = weather_data['current']['temp']
    
    await update.message.reply_text(
        f"{location} için hava durumu:\n"
        f"🌡️ Sıcaklık: {temp}°C\n"
        f"☁️ Durum: {weather_data['current']['weather'][0]['description']}"
    )

def run_bot(token: str):
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", get_weather))
    app.run_polling()