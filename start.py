# -*- coding: utf-8 -*-
import os
import sys

from irbot.irbot import IngressoRapidoBot


if __name__ == '__main__':
    token = os.environ.get('IRBOT_TOKEN', '')

    # Se o token não foi configurado como variável de ambiente,
    # encerramos o programa sem lançar o bot
    if not token:
        sys.stderr.write('Erro: variável de ambiente IRBOT_TOKEN não está configurada.')
        sys.exit(1)

    IngressoRapidoBot(token).run()
