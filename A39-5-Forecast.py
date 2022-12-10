import requests
import json
import pprint

apiKey = '6ZxEsAOjNyT0h2EnC5rQlW8Brg4tCGtB'

def getCoordinates():
    r = requests.get('http://www.geoplugin.net/json.gp')
    if(r.status_code != 200):
        print('Não foi possível obter a localização (coordinates')
        return None
    else:
        try:
            location = json.loads(r.text)
            print(pprint.pprint(location))
        except:
            print('Error on get coordinates')

getCoordinates()