import discord
from discord.ext import commands
from services.weather_api import WeatherFetcher

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} bağlandı!')

@bot.command()
async def hava(ctx, *, location: str):
    weather_data = WeatherFetcher.get_weatherapi(location)
    await ctx.send(
        f"🌦️ {location} için hava durumu:\n"
        f"Sıcaklık: {weather_data['current']['temp_c']}°C\n"
        f"Durum: {weather_data['current']['condition']['text']}"
    )

def run_bot(token: str):
    bot.run(token)