from aiogram import types
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from buttons import MAIN_MENU_BUTTON
from exceptions import UpdateGoogleError
from states import AdminFSM


async def update_data(_: types.CallbackQuery,
                      __: Button,
                      manager: DialogManager):
    raise UpdateGoogleError


admin_dialog = Dialog(
    Window(
        Const("Выберите действие"),
        Button(
            text=Const("Обновить данные"),
            id="update_data",
            on_click=update_data
        ),
        MAIN_MENU_BUTTON,
        state=AdminFSM.state
    )
)
