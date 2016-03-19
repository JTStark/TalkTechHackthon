from .busca_ingresso_rapido import search_event_by_name

def event_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Event handler response")

def start_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi!")

def search_handler(bot, update):
    param = update.message.text.split()
    param.pop(0)
    searchStr = ' '.join(param)
    events = search_event_by_name(event=searchStr)
    counter = 0
    for event in events:
        counter = counter + 1
        bot.sendMessage(chat_id=update.message.chat_id, text=event['title'])
        # bot.sendPhoto(chat_id=update.message.chat_id, photo=event['image_url'])
        bot.sendMessage(chat_id=update.message.chat_id, text=event['event_url'])
        if counter == 3:
            break
            """
            bot.sendMessage(chat_id=update.message.chat_id, text='Mais eventos?')
            counter = 0
            """
