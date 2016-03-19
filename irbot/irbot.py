# -*- coding: utf-8 -*-

from telegram import Updater

from .commands import start_handler
from .commands import search_handler
from .commands import events_on_handler
from .commands import events_at_handler
from .commands import events_type_handler
from .commands import events_between_handler
from .commands import more_handler
from .commands import shows_handler
from .commands import cinema_handler
from .commands import dance_handler
from .commands import classicos_handler
from .commands import parties_handler
from .commands import sports_handler
from .commands import theater_handler

class IngressoRapidoBot(object):

    # Mapa de comandos -> funções de tratamento
    commands = {
        'start': start_handler,
	'eventosnodia': events_on_handler,
        'eventosem': events_at_handler,
        'eventosdotipo': events_type_handler,
        'busca': search_handler,
	'eventosnoperiodo': events_between_handler,
        'mais': more_handler,
        'shows': shows_handler,
        'festas': parties_handler,
        'cinema': cinema_handler,
        'esportes': sports_handler,
        'teatro': theater_handler
    }

    def __init__(self, token):
        self.updater = Updater(token=token)
        dispatcher = self.updater.dispatcher

        for cmd, cmd_handler in self.commands.iteritems():
            dispatcher.addTelegramCommandHandler(cmd, cmd_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
