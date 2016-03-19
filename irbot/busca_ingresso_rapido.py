SITE_URL = 'https://www.ingressorapido.com.br/'

mock_event = {
    'event_url': SITE_URL + 'Evento.aspx?ID=46865',
    'image_url': SITE_URL + 'ImagensSistema/Eventos/eI047372thumb.jpg',
    'title': 'Titulo',
    'local': 'Lugar',
    'pages': 1
}

def search_event_by_name(event, page_number=1):
    return [mock_event]

def search_event_by_city(city, page_number=1):
    return [mock_event]

def search_event_by_category(category, page_number=1):
    return [mock_event]

def search_event_by_date(start_date, end_date, page_number=1):
    return [mock_event]
