from aiogram import types
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const


async def update_data(_: types.CallbackQuery,
                      __: Button,
                      manager: DialogManager):
    ...


admin_dialog = Dialog(
    Window(
        Const("Выберите действие"),
        Button(
            text=Const("Обновить данные"),
            id="update_data",
            on_click=update_data
        ),
        state=...
    )
)
