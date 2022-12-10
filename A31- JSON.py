import requests
import json
import pprint

r = requests.get('http://www.geoplugin.net/json.gp')
if (r.status_code != 200):
    print('Não foi possível obter a localização.')
else:
    location = json.loads(r.text)
    long = location['geoplugin_longitude']
    lat = location['geoplugin_latitude']
    # print(pprint.pprint(location)) # Para visualizar de forma mais fácil
    print('Latitude:', long)
    print('Longitude:',lat)