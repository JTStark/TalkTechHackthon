from .busca_ingresso_rapido import search_event_by_name
from .busca_ingresso_rapido import search_event_by_date
from .busca_ingresso_rapido import search_event_by_city
from .busca_ingresso_rapido import search_event_by_category

def event_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Event handler response")

def start_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Procure o melhor evento para você!\n")
    bot.sendMessage(chat_id=update.message.chat_id, text="/eventosnodia Receba os eventos que ocorrerao em um determinado dia.")
    bot.sendMessage(chat_id=update.message.chat_id, text="/eventosem Procure por eventos que ocorrerao em uma cidade.")
    bot.sendMessage(chat_id=update.message.chat_id, text="/eventosdotipo Procure por eventos de acordo com seu estilo")
    bot.sendMessage(chat_id=update.message.chat_id, text="/busca Busque eventos por palavra chave")
    bot.sendMessage(chat_id=update.message.chat_id, text="/eventosnoperiodo Busque eventos em um determinado periodo")


def search_handler(bot, update):
    chat_id = update.message.chat_id
    param = update.message.text.split(' ', 1)
    param.pop(0)
    if len(param) == 0:
        msg = 'Digite o nome do evento ou local para buscar.'
        bot.sendMessage(chat_id=chat_id, text=msg)
    else:
        events = search_event_by_name(event=searchStr)
        leng = len(events)
        for i in xrange(3):
            if i < leng:
                msg = events[i]['title'] + ', em ' + events[i]['local'] + '\n' + events[i]['event_url']
                bot.sendMessage(chat_id=update.message.chat_id, text=msg)
#               bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
                # bot.sendPhoto(chat_id=update.message.chat_id, photo=event['image_url'])
        
        if leng > 3:
            bot.sendMessage(chat_id=update.message.chat_id, text='Mais eventos? Use /more')
            
def events_on_handler(bot, update):
    date = update.message.text.split()
    event = search_event_by_date(date[1], date[1])
    leng = len(event)
    for i in xrange(3):
        if i < leng:
            bot.sendMessage(chat_id=update.message.chat_id, text=event[i]["title"] + ', em ' + event[i]['local'] + '\n' + event[i]["event_url"])
#           bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    
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
            bot.sendMessage(chat_id=update.message.chat_id, text=event[i]["title"] + ', em ' + event[i]['local'] + '\n' + event[i]["event_url"])
#           bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /more")

def events_at_handler(bot, update):
    city = update.message.text.split(' ', 1)
    response = search_event_by_city(city[1])
    leng = len(response)
    for i in xrange(3):
        if i < leng:
	    bot.sendMessage(chat_id=update.message.chat_id, text=response[i]["title"] + ', em ' + response[i]['local'] + '\n' + response[i]["event_url"])
#    	    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /more")	

def events_type_handler(bot, update):
    category = update.message.text.split(' ', 1)
    categories = {
        'Cinema' : "10",
        'Classicos' : "28",
        'Concerto' : "29",
        'Danca' : "9",
        'Especiais' : "25",
        'Esporte' : "6",
        'Festas' : "5",
        'Futebol' : "40",
        'Infantil e Familiares' : "18",
        'Jazz' : "30",
        'Show' : "2",
        'Teatro' : "1"
    }
    response = search_event_by_category(categories[category[1]])
    leng = len(response)
    for i in xrange(3):
        if i < leng:
	    bot.sendMessage(chat_id=update.message.chat_id, text=response[i]["title"] + ', em ' + response[i]['local'] + '\n' + response[i]["event_url"])
#   	    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /more")
