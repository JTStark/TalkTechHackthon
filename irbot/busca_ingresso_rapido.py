from bs4 import BeautifulSoup
import requests

SITE_URL = 'https://www.ingressorapido.com.br/'

mock_event = {
    'event_url': SITE_URL + 'Evento.aspx?ID=46865',
    'image_url': SITE_URL + '/ImagensSistema/Eventos/eI047372thumb.jpg',
    'title': 'Titulo',
    'local': 'Lugar',
    'pages': 1
}

def search_event_by_name(event_name, page_number=1):
    r = requests.get("http://www.ingressorapido.com.br/BuscaPrincipal.aspx?pesq=" + event_name)
    return parse_reponse(r)


def search_event_by_city(city, page_number=1):
    r = requests.get("https://www.ingressorapido.com.br/eventos.aspx?cidade=" + city)
    return parse_reponse(r)

def search_event_by_category(category, page_number=1):
    r = requests.get("https://www.ingressorapido.com.br/eventos.aspx?categoria=" + category)
    return parse_reponse(r)

def search_event_by_date(start_date, end_date, page_number=1):
    r = requests.get("https://www.ingressorapido.com.br/eventos.aspx?dataDe=" + start_date + "&dataAte=" + end_date)
    return parse_reponse(r)

def parse_reponse(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    events = []
    for table in soup.find_all('table', class_='boxDotBorder'):
        event = {}
        event['image_url'] = str(table.img.get('src'))
        event['event_url'] = str(SITE_URL + table.select('a')[1].get('href'))
        event['title'] = str(table.select('a')[1].text.encode('utf-8'))
        li = table.select('li')
        span = table.select('span')
        if(len(li) > 2):
            event['local'] = str(li[1].text.encode('utf-8') + ' - ' + li[2].text.encode('utf-8'))
        else:
            event['local'] = str(span[0].text.encode('utf-8'))
        events.append(event)

    return events
