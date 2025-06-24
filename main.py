import logging
from asyncio import run
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from core.config import TOKEN, DEVELOPER
from core.table_queries import initializing_tables
from routers import common, register, feedback, backs
from utils.commands import set_my_commands


async def startup(bot: Bot):
    initializing_tables()
    await set_my_commands(bot)
    # await bot.send_message(text="Bot start to work", chat_id=DEVELOPER)


async def shutdown(bot: Bot):
    await bot.send_message(text="Bot stopped", chat_id=DEVELOPER)


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(router=common.router)
    dp.include_router(router=register.router)
    dp.include_router(router=feedback.router)
    dp.include_router(router=backs.router)

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot, polling_timeout=0)


if __name__ == '__main__':
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    run(main())
