from aiogram import Dispatcher, BaseMiddleware


def register_middlewares(middlewares: list[BaseMiddleware],
                         dispatcher: Dispatcher):
    for middleware in middlewares:
        dispatcher.update.middleware(middleware)
        dispatcher.error.middleware(middleware)
