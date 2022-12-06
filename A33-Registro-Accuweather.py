import requests
import json
import pprint
accuwweatherAPIKey = '6ZxEsAOjNyT0h2EnC5rQlW8Brg4tCGtB'

r = requests.get('http://www.geoplugin.net/json.gp')
if (r.status_code != 200):
    print('Não foi possível obter a localização.')
else:
    location = json.loads(r.text)
    long = location['geoplugin_longitude']
    lat = location['geoplugin_latitude']
    # print(pprint.pprint(location)) # Para visualizar de forma mais fácil
    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuwweatherAPIKey + "&q=" + lat + "%2C" + long + "&language=pt-br"

    r2 = requests.get(locationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a localização.')
    else:
        print(pprint.pprint(json.loads(r2.text)))