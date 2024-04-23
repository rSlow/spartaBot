from aiogram import Bot, Dispatcher

from .logger import init_logging


async def on_startup(dispatcher: Dispatcher,
                     bot: Bot):
    init_logging()
