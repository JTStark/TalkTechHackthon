# -*- coding: utf-8 -*-

from telegram import Updater

from .commands import event_handler
from .commands import start_handler
from .commands import search_handler
from .commands import events_on_handler
from .commands import events_at_handler

class IngressoRapidoBot(object):

    # Mapa de comandos -> funções de tratamento
    commands = {
        'event': event_handler,
        'start': start_handler,
        'search': search_handler
	'eventsOn': events_on_handler,
        'eventsAt': events_at_handler
    }

    def __init__(self, token):
        self.updater = Updater(token=token)
        dispatcher = self.updater.dispatcher

        for cmd, cmd_handler in self.commands.iteritems():
            dispatcher.addTelegramCommandHandler(cmd, cmd_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
