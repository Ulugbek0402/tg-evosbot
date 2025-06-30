import os

from dotenv import load_dotenv

load_dotenv(
    dotenv_path=".env"
)

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

TOKEN = os.getenv("TOKEN")

BASE_WEBHOOK_URL = os.getenv("BASE_WEBHOOK_URL")

DEVELOPER = 1987023564
ADMINS = [1987023564]

I18N_DOMAIN = 'lang'
LOCALES_DIR = 'locale'

CHANNELS = [
    {
        "name": "Channel 1",
        "link": "https://t.me/https://t.me/for_bot_test",
        "chat_id": -1002848846009
    }
]