from .busca_ingresso_rapido import search_event_by_date
from .busca_ingresso_rapido import search_event_by_city


def event_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Event handler response")

def start_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi!")

def events_on_handler(bot, update):
    date = update.message.text.split()
    event = search_event_by_date(date[1], date[1])
    bot.sendMessage(chat_id=update.message.chat_id, text=event[0]["title"] + '\n' + event[0]["event_url"])
    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')

#    bot.sendMessage(chat_id=update.message.chat_id, text="Coldplay Show, at Allianz Parque, on Fri, April 1st\nhttps://example.com")
#    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')

def events_at_handler(bot, update):
	city = update.message.text.split(' ', 1)
	response = search_event_by_city(city[1])
	bot.sendMessage(chat_id=update.message.chat_id, text=response[0]["title"] + '\n' + response[0]["event_url"])
	bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')	
