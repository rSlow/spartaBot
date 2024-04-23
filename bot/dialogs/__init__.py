from aiogram import Router

from .main import main_dialog
from .places_by_type import competitions_dialog

dialogs_router = Router(name="dialogs")

dialogs_router.include_routers(
    main_dialog,
    competitions_dialog,
)
