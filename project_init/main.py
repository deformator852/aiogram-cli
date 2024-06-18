import os


def create_main(project_path):
    with open(project_path + "/main.py", "w") as file:
        file.write(
            """from create_bot import dp, bot
import asyncio
import logging
import sys


async def main():
    dp.include_router()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

"""
        )
