# -*- coding: utf-8 -*-
from .busca_ingresso_rapido import search_event_by_name
from .busca_ingresso_rapido import search_event_by_date
from .busca_ingresso_rapido import search_event_by_city
from .busca_ingresso_rapido import search_event_by_category
from .util import take

LAST_COMMAND = None
MORE_DATA = None


def render_msg(bot, update, msg):
    bot.sendMessage(chat_id=update.message.chat_id, text=msg)

def more_handler(bot, update):
    if not MORE_DATA:
        render_msg(bot, update, "Ops, parece que não tenho mais resultados para te mostrar. Tente fazer outra busca.")
        return
    if LAST_COMMAND == 'search':
        render_search_events_msg(MORE_DATA)

"""
def render_search_events_msg(bot, update, events):
    sys.stderr.write(str(len(events)) + '\n')
    for i in xrange(3):
        if i < len(events):
            msg = events[i]['title'] + ', em ' + events[i]['local'] + '\n' + events[i]['event_url']
            render_msg(bot, update, msg)
    if len(events) > 3:
        MORE_DATA = events[3:]
        LAST_COMMAND = 'search'
        render_msg(bot, update, 'Quer ver mais eventos? Use /mais')
"""

def start_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Procure o melhor evento para você!\n")
    bot.sendMessage(chat_id=update.message.chat_id, text="/eventosnodia Receba os eventos que ocorrerao em um determinado dia.")
    bot.sendMessage(chat_id=update.message.chat_id, text="/eventosem Procure por eventos que ocorrerao em uma cidade.")
    bot.sendMessage(chat_id=update.message.chat_id, text="/eventosdotipo Procure por eventos de acordo com seu estilo")
    bot.sendMessage(chat_id=update.message.chat_id, text="/busca Busque eventos por palavra chave")
    bot.sendMessage(chat_id=update.message.chat_id, text="/eventosnoperiodo Busque eventos em um determinado periodo")



def search_handler(bot, update):
    try:
        search_string = update.message.text.split(' ', 1)[1]
        import sys

        sys.stderr.write(search_string + '\n')
        events = search_event_by_name(event_name=search_string)
        if len(events) == 0:
            sys.stderr.write('Hi\n')
            render_msg(bot, update, 'Nenhum evento com esse nome')
        else:
            sys.stderr.write(str(events) + '\n')
            #render_search_events_msg(events)
            sys.stderr.write(not events)
            for i in xrange(3):
                if i < len(events):
                    msg = events[i]['title'] + ', em ' + events[i]['local'] + '\n' + events[i]['event_url']
                    render_msg(bot, update, msg)
            if len(events) > 3:
                MORE_DATA = events[3:]
                LAST_COMMAND = 'search'
                render_msg(bot, update, 'Quer ver mais eventos? Use /mais')
    except IndexError:
        render_msg(bot, update, 'Preciso que você me diga o que está buscando!')


def events_on_handler(bot, update):
    date = update.message.text.split()
    event = search_event_by_date(date[1], date[1])
    leng = len(event)
    for i in xrange(3):
        if i < leng:
            bot.sendMessage(chat_id=update.message.chat_id, text=event[i]["title"] + ', em ' + event[i]['local'] + '\n' + event[i]["event_url"])
#           bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')

    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /mais")

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
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /mais")

def events_at_handler(bot, update):
    city = update.message.text.split(' ', 1)
    response = search_event_by_city(city[1])
    leng = len(response)
    for i in xrange(3):
        if i < leng:
	    bot.sendMessage(chat_id=update.message.chat_id, text=response[i]["title"] + ', em ' + response[i]['local'] + '\n' + response[i]["event_url"])
#    	    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /mais")

def events_type_handler(bot, update):
    category = update.message.text.split(' ', 1)
    render_events_by_category(bot, update, category[1])

def render_events_by_category(bot, update, category):
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

    response = search_event_by_category(categories[category])
    leng = len(response)
    for i in xrange(3):
        if i < leng:
	    bot.sendMessage(chat_id=update.message.chat_id, text=response[i]["title"] + ', em ' + response[i]['local'] + '\n' + response[i]["event_url"])
#   	    bot.sendPhoto(chat_id=update.message.chat_id, photo='http://f.i.uol.com.br/folha/ilustrada/images/15324369.jpeg')
    if leng > 3:
        bot.sendMessage(chat_id=update.message.chat_id, text="Mais eventos? Use /mais")


def shows_handler(bot, update):
    render_events_by_category(bot, update, "Show")

def cinema_handler(bot, update):
    render_events_by_category(bot, update, "Cinema")

def dance_handler(bot, update):
    render_events_by_category(bot, update, "Danca")

def classicos_handler(bot, update):
    render_events_by_category(bot, update, 'Classicos')

def concert_handler(bot, update):
    render_events_by_category(bot, update, "Concerto")

def parties_handler(bot, update):
    render_events_by_category(bot, update, "Festas")

def sports_handler(bot, update):
    render_events_by_category(bot, update, "Esporte")

def theater_handler(bot, update):
    render_events_by_category(bot, update, "Teatro")
