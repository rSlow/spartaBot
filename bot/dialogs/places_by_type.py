from operator import itemgetter

from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.text import Const, Format
from sqlalchemy.ext.asyncio import AsyncSession

from buttons import MAIN_MENU_BUTTON
from states import CompetitionFSM


async def competitions_getter(dialog_manager: DialogManager, **__):
    # session: AsyncSession = dialog_manager.middleware_data["session"]
    return {
        "competitions": [("Эстафета", 1), ("Русский жим", 2)]
    }


competitions_dialog = Dialog(
    Window(
        Const("Выберите вид соревнований:"),
        Select(
            text=Format("{item[0]}"),
            item_id_getter=itemgetter(1),
            id="competitions",
            items="competitions"
        ),
        MAIN_MENU_BUTTON,
        getter=competitions_getter,
        state=CompetitionFSM.state
    )
)
