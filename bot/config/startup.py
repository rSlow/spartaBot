from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from .logger import init_logging

from aiogram_dialog import setup_dialogs
from dialogs import dialogs_router
from handlers.commands import commands_router
from handlers.errors import error_router
from .middlewares import register_middlewares


async def on_startup(dispatcher: Dispatcher,
                     bot: Bot):
    init_logging()

    setup_dialogs(dispatcher)
    dispatcher.include_routers(
        commands_router,
        error_router,
        dialogs_router,
    )

    register_middlewares(
        middlewares=[CallbackAnswerMiddleware()],
        dispatcher=dispatcher
    )
