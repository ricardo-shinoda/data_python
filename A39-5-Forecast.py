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
            # print(pprint.pprint(location)) # to look at the api output
            coordinate = {}
            coordinate['long'] = location['geoplugin_longitude']
            coordinate['lat'] = location['geoplugin_latitude']
            print(coordinate['long'])
            print(coordinate['lat'])
            return coordinate
        except:
            print('Error on get coordinates')

def localCode(lat, long):
    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + apiKey + "&q=" + lat + "%2C" + long + "&language=pt-br"
    r = requests.get(locationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a localização (localCode)')
        return None
    else:
        locationResponse = (json.loads(r.text))
        print(pprint.pprint(locationResponse))
        localInfo = {}
        localInfo['localName'] = locationResponse['LocalizedName'] + " , " + locationResponse['AdministrativeArea']['LocalizedName'] + ", " + locationResponse['Country']['LocalizedName']
        localInfo['localCode'] = locationResponse['Key']
        return localInfo

coordinates = getCoordinates()
local = localCode(coordinates['lat'], coordinates['long'])