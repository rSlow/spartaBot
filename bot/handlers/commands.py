from aiogram import Router, types
from aiogram.filters import Command
from aiogram_dialog import DialogManager, StartMode, ShowMode

from states import StartFSM

commands_router = Router(name="commands")


@commands_router.message(Command("start"))
async def start(_: types.Message,
                dialog_manager: DialogManager):
    await dialog_manager.start(
        state=StartFSM.state,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND
    )
