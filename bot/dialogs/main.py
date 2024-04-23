from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from states import StartFSM, CompetitionFSM, AdminFSM

main_dialog = Dialog(
    Window(
        Const("Добро пожаловать. Выберите действие:"),
        Start(
            text=Const("Таблица результатов"),
            id="results_table",
            state=...
        ),
        Start(
            text=Const("Места по видам"),
            id="places_by_type",
            state=CompetitionFSM.state
        ),
        Start(
            text=Const("Админка"),
            id="admin",
            state=AdminFSM.state
        ),
        state=StartFSM.state
    )
)
