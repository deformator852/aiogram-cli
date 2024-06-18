import os


def create_bot(project_path):
    with open(project_path + "/create_bot.py", "w") as file:
        file.write(
            """from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import os

TOKEN = ""
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
"""
        )
