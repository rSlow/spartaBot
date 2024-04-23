from aiogram import types, F, Router
from aiogram.filters import ExceptionTypeFilter
from aiogram_dialog import DialogManager

from exceptions import UpdateGoogleError

error_router = Router(name="errors")


@error_router.error(
    ExceptionTypeFilter(UpdateGoogleError),
    F.update.event.message.as_("message")
)
async def update_error(_: types.ErrorEvent,
                       message: types.Message,
                       dialog_manager: DialogManager,
                       **__):
    ...
