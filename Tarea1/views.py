from django.http import HttpResponse, HttpRequest
from django.template import Template, Context, loader
from random import randint
import requests 

def index(request):
    response = requests.get("https://rickandmortyapi.com/api/character/")
    characters = response.json()
    aux = characters['info']
    while aux['next'] != '':
        response = requests.get(aux['next'])
        aux = response.json()
        for i in aux['results']:
            characters['results'].append(i)
        aux = aux['info'] 

    show = list()
    for i in range(6):
        values = randint(0, characters['info']['count'] - 1)
        show.append(values)

    ch = [d for d in characters['results'] if d['id'] in show]
    aux2 = dict()
    for i in range(0, len(ch)):
        aux2['image{}'.format(i)] = (ch[i]['image'])
        aux2['name{}'.format(i)] = (ch[i]['name'])
    
    response = requests.get("https://rickandmortyapi.com/api/episode/")
    episodes = response.json()
    ep_list = list ()
    for i in episodes['results']:
        episode = dict()
        episode['id'] = i['id']
        episode['name'] = i['name']
        episode['air_date'] = i['air_date']
        episode['episode'] = i['episode']
        ep_list.append(episode)
    aux = episodes['info']
    
    count = 1
    while aux['next'] != '':
        response = requests.get(aux['next'])
        aux = response.json()
        for i in aux['results']:
            episode = dict()
            episode['id'] = i['id']
            episode['name'] = i['name']
            episode['air_date'] = i['air_date']
            episode['episode'] = i['episode']
            ep_list.append(episode)
            count += 1
        aux = aux['info'] 

    aux2['ep_list'] = ep_list

    doc_externo = loader.get_template('index.html')
    documento = doc_externo.render(aux2)

    return HttpResponse(documento)

def contact(request):

    doc_externo = loader.get_template('contact.html')

    documento = doc_externo.render({})

    return HttpResponse(documento)

def episode(request, **kwargs):
    response = requests.get("https://rickandmortyapi.com/api/episode/{}".format(str(kwargs['number'])))
    episode = response.json()
    show = list()
    for i in episode['characters']:
        character = i.split('/')
        show.append(int(character[5]))

    l_characters = list()
    response = requests.get("https://rickandmortyapi.com/api/character/")
    characters = response.json()
    for i in characters['results']:
        if i['id'] in show:
            l_characters.append(i)
    aux = characters['info']
    while aux['next'] != '':
        response = requests.get(aux['next'])
        aux = response.json()
        for i in aux['results']:
            if i['id'] in show:
                l_characters.append(i)
        aux = aux['info'] 

    episode['characters'] = l_characters

    doc_externo = loader.get_template('episode.html')
    documento = doc_externo.render(episode)

    return HttpResponse(documento)

def character(request, **kwargs):
    response = requests.get("https://rickandmortyapi.com/api/character/{}".format(str(kwargs['number'])))
    character = response.json()

    if character['location']['url'] != '':
        location_show_id = int(character['location']['url'].split("/")[5])
    else:
        location_show_id = ''
    location_show_name = character['location']['name']
    if character['origin']['url'] != '':
        origin_show_id = int(character['origin']['url'].split("/")[5])
    else:
        origin_show_id = ''
    origin_show_name = character['origin']['name']
    
    ep_list = list()
    for i in character['episode']:
        values = int(i.split("/")[5])
        ep_list.append(values)
    
    aux2 = list()
    for i in ep_list:
        response = requests.get("https://rickandmortyapi.com/api/episode/{}".format(i))
        episode = response.json()
        aux = dict()
        aux['id'] = episode['id']
        aux['name'] = episode['name']
        aux['air_date'] = episode['air_date']
        aux['episode'] = episode['episode']
        aux2.append(aux)
        
    aux3 = dict()
    aux3['name'] = character['name']
    aux3['status'] = character['status']
    aux3['species'] = character['species']
    aux3['type'] = character['type']
    aux3['gender'] = character['gender']
    aux3['image'] = character['image']
    aux3['location_show_id'] = location_show_id
    aux3['origin_show_id'] = origin_show_id
    aux3['location_show_name'] = location_show_name
    aux3['origin_show_name'] = origin_show_name
    aux3['ep_list'] = aux2

    doc_externo = loader.get_template('character.html')
    documento = doc_externo.render(aux3)

    return HttpResponse(documento)

def location(request, **kwargs):
    response = requests.get("https://rickandmortyapi.com/api/location/{}".format(str(kwargs['number'])))
    location = response.json()
    
    ch_list = list()
    for i in location['residents']:
        values = int(i.split("/")[5])
        ch_list.append(values)

    aux2 = list()
    for i in ch_list:
        response = requests.get("https://rickandmortyapi.com/api/character/{}".format(i))
        character = response.json()
        aux = dict()
        aux['id'] = character['id']
        aux['name'] = character['name']
        aux['image'] = character['image']
        aux2.append(aux)

    aux3 = dict()
    aux3['name'] = location['name']
    aux3['type'] = location['type']
    aux3['dimension'] = location['dimension']
    aux3['ch_list'] = aux2

    doc_externo = loader.get_template('location.html')
    documento = doc_externo.render(aux3)

    return HttpResponse(documento)

def episodes(request):
    
    response = requests.get("https://rickandmortyapi.com/api/episode/")
    episod = response.json()
    ep_list = list ()
    for i in episod['results']:
        episode = dict()
        episode['id'] = i['id']
        episode['name'] = i['name']
        episode['air_date'] = i['air_date']
        episode['episode'] = i['episode']
        ep_list.append(episode)
    aux = episod['info']
    aux2 = dict()
    count = 1
    while aux['next'] != '':
        response = requests.get(aux['next'])
        aux = response.json()
        for i in aux['results']:
            episode = dict()
            episode['id'] = i['id']
            episode['name'] = i['name']
            episode['air_date'] = i['air_date']
            episode['episode'] = i['episode']
            ep_list.append(episode)
            count += 1
        aux = aux['info'] 

    aux2['ep_list'] = ep_list

    doc_externo = loader.get_template('episodes.html')
    documento = doc_externo.render(aux2)

    return HttpResponse(documento)

def characters(request):
    response = requests.get("https://rickandmortyapi.com/api/character/")
    characters = response.json()
    aux = characters['info']
    while aux['next'] != '':
        response = requests.get(aux['next'])
        aux = response.json()
        for i in aux['results']:
            characters['results'].append(i)
        aux = aux['info'] 

    aux2 = list()
    for i in characters['results']:
        aux3 = dict()
        aux3['image'.format(i)] = (i['image'])
        aux3['id'.format(i)] = (i['id'])
        aux3['name'.format(i)] = (i['name'])
        aux2.append(aux3)
    
    aux4 = dict()
    aux4['characters'] = aux2
    doc_externo = loader.get_template('characters.html')
    documento = doc_externo.render(aux4)

    return HttpResponse(documento)

def locations(request):
    response = requests.get("https://rickandmortyapi.com/api/location/")
    loc = response.json()
    loc_list = list ()
    for i in loc['results']:
        location = dict()
        location['id'] = i['id']
        location['name'] = i['name']
        location['type'] = i['type']
        location['dimension'] = i['dimension']
        loc_list.append(location)
    aux = loc['info']
    aux2 = dict()
    count = 1
    while aux['next'] != '':
        response = requests.get(aux['next'])
        aux = response.json()
        for i in aux['results']:
            location = dict()
            location['id'] = i['id']
            location['name'] = i['name']
            location['type'] = i['type']
            location['dimension'] = i['dimension']
            loc_list.append(location)
            count += 1
        aux = aux['info'] 

    aux2['loc_list'] = loc_list

    doc_externo = loader.get_template('locations.html')
    documento = doc_externo.render(aux2)

    return HttpResponse(documento)