from bots.telegram_bot import run_bot as run_telegram_bot
from bots.discord_bot import run_bot as run_discord_bot
from threading import Thread
import os

if __name__ == "__main__":
    # Paralel çalıştırma
    Thread(target=run_telegram_bot, args=(os.getenv("TELEGRAM_TOKEN"),)).start()
    Thread(target=run_discord_bot, args=(os.getenv("DISCORD_TOKEN"),)).start()