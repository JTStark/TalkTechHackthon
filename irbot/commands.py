from .busca_ingresso_rapido import search_event_by_name
from .busca_ingresso_rapido import search_event_by_date
from .busca_ingresso_rapido import search_event_by_city
from .busca_ingresso_rapido import search_event_by_category

def event_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Event handler response")

def start_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi!")

def search_handler(bot, update):
    param = update.message.text.split(' ', 1)
    param.pop(0)
    #searchStr = ' '.join(param)
    events = search_event_by_name(event=searchStr)
    leng = len(events)
    for i in xrange(3):
        msg = events[i]['title'] + '\n' + events[i]['event_url']
        bot.sendMessage(chat_id=update.message.chat_id, text=msg)
        bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
        # bot.sendPhoto(chat_id=update.message.chat_id, photo=event['image_url'])
        
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text='Mais eventos? Use /more')
            
def events_on_handler(bot, update):
    date = update.message.text.split()
    event = search_event_by_date(date[1], date[1])
    leng = len(event)
    for i in xrange(3):
        if i < leng:
            bot.sendMessage(chat_id=update.message.chat_id, text=event[i]["title"] + '\n' + event[i]["event_url"])
            bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /more")

#    bot.sendMessage(chat_id=update.message.chat_id, text="Coldplay Show, at Allianz Parque, on Fri, April 1st\nhttps://example.com")
#    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')

def events_between_handler(bot, update):
    date = update.message.text.split()
    event = search_event_by_date(date[1], date[2])
    leng = len(event)
    for i in xrange(3):
        if i < leng:
            bot.sendMessage(chat_id=update.message.chat_id, text=event[i]["title"] + '\n' + event[i]["event_url"])
            bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /more")

def events_at_handler(bot, update):
    city = update.message.text.split(' ', 1)
    response = search_event_by_city(city[1])
    leng = len(response)
    for i in xrange(3):
        if i < leng:
	    bot.sendMessage(chat_id=update.message.chat_id, text=response[i]["title"] + '\n' + response[i]["event_url"])
    	    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /more")	

def events_type_handler(bot, update):
    category = update.message.text.split(' ', 1)
    response = search_event_by_category(category[1])
    leng = len(response)
    for i in xrange(3):
        if i < leng:
	    bot.sendMessage(chat_id=update.message.chat_id, text=response[i]["title"] + '\n' + response[i]["event_url"])
    	    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /more")	



