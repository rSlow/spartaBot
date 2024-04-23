from abc import abstractmethod
from typing import Protocol

from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


class OnButtonClick(Protocol):
    @abstractmethod
    def __call__(self,
                 _: types.CallbackQuery,
                 __: Button,
                 manager: DialogManager):
        ...
