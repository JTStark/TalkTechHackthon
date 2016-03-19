# IngressoRápido Bot

Repositório com nossa implementação do bot para o Hackaton.

## Instalando as dependências

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

Instalando as dependências:

```
pip install -r requirements.txt
```

## Rodando o bot

Nosso bot lê seu token a partir de uma variável de ambiente chamada `IRBOT_TOKEN`.

Para iniciar o bot:

```
export IRBOT_TOKEN="<token>"; python start.py
```
