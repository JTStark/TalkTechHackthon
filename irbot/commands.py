def event_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Event handler response")

def start_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi!")
