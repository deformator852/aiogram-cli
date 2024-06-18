import os


def create_keyboards(project_path):
    with open(project_path + "/keyboards.py", "w") as file:
        file.write(
            """from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder"""
        )
