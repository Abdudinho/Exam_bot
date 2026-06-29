from os import getenv

from dotenv import load_dotenv
load_dotenv()


class BotEnv:
    BOT_TOKEN = getenv('BOT_TOKEN')
    PAYMENT_TOKEN =  getenv('PAYMENT_TOKEN')

class DatabaseEnv:
    DB_NAME = getenv("DB_NAME")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_HOST = getenv("DB_HOST")
    DB_PORT = getenv("DB_PORT")

class WebEnv:
    ADMIN_NAME = getenv("ADMIN_NAME")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD")

class Env:
    bot = BotEnv()
    db = DatabaseEnv()
    web = WebEnv()
