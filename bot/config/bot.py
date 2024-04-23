from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram_dialog import setup_dialogs

from config import settings
from config.shutdown import on_shutdown
from config.startup import on_startup
from config.storage import redis_storage
from dialogs.main import main_dialog
from handlers.commands import commands_router

dispatcher = Dispatcher(
    storage=redis_storage,
    events_isolation=SimpleEventIsolation()
)
bot = Bot(
    token=settings.BOT_TOKEN,
    parse_mode=ParseMode.HTML,
)


def init_dispatcher(dp: Dispatcher):
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    setup_dialogs(dp)

    dp.include_routers(
        commands_router,
        main_dialog,
    )
