from config.bot import dispatcher, bot, init_dispatcher

if __name__ == '__main__':
    init_dispatcher(dispatcher)
    dispatcher.run_polling(bot)
