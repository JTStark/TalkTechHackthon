# IngressoRápido Bot

Repositório com nossa implementação do bot para o Hackaton.

## Instalando o bot

É necessário ter o PIP instalado:

```
apt-get update && apt-get install python-pip
```

### Virtualenv

Usamos o `virtualenv` para que os pacotes instalados como dependências do
bot não interfiram com os pacotes globais do sistem:

```
pip install virtualenv
```

Criamos um `virtualenv`:

```
virtualenv venv
```

Ativamos o ambiente virtual:

```
source venv/bin/activate
```

Instalando o bot:

```
pip install .
```

## Rodando o bot

Nosso bot lê seu token a partir de uma variável de ambiente chamada `IRBOT_TOKEN`
ou fornecer o token como parâmetro para o script que inicia o bot.

Para iniciar o bot:

```
IRBOT_TOKEN="<token>" irbot
```

ou

```
irbot --token "<token>"
```

## Desinstalando o bot

Novamente, usando pip:

```
pip uninstall irbot
```
