import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Not specified TELEGRAM_BOT_TOKEN")