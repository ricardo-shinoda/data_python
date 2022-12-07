import requests
import json
# import pprint

accuweatherAPIKey = '6ZxEsAOjNyT0h2EnC5rQlW8Brg4tCGtB' # API Key para acessar a api accuWeather

def getCoordinates(): # To get Coordinates
    r = requests.get('http://www.geoplugin.net/json.gp') # url da api
    if (r.status_code != 200):
        print('Não foi possível obter a localização (r).')
    else:
        location = json.loads(r.text) # transformar o request da api em Json
        coordinate = {}
        coordinate['long'] = location['geoplugin_longitude'] # acessando a longitude
        coordinate['lat'] = location['geoplugin_latitude'] # acessando a latitude
        # print(pprint.pprint(location)) # Para visualizar de forma mais fácil
        return coordinate

def getLocalCode(lat, long):
    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherAPIKey + "&q=" + lat + "%2C" + long + "&language=pt-br" # endereço da pi com a Key, latitude e longitude

    r = requests.get(locationAPIUrl) # acessando a api com o key para obter o código do local (key)
    if (r.status_code != 200):
        print('Não foi possível obter a localização (r2).')
    else:
        locationResponse = (json.loads(r.text)) # transformando o response em json
        localInfo = {}
        localInfo['nomeLocal'] = locationResponse['LocalizedName'] + "," + locationResponse['AdministrativeArea']['LocalizedName'] + "." + locationResponse['Country']['LocalizedName']
        localInfo['codigoLocal'] = locationResponse['Key']
        return localInfo

def getCurrentWeather(localCode, localName):

    CurrentConditionAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + localCode + "?apikey=" + accuweatherAPIKey + "&language=pt-br"

    r = requests.get(CurrentConditionAPIUrl) # Acessando outra api para obter a temperatura com a chave do local obtido na requisição anterior.
    if (r.status_code != 200):
        print('Não foi possível obter a localização (r3).')
    else:
        CurrentConditionResponse = (json.loads(r.text))
        weatherInfo = {}
        # print(pprint.pprint(CurrentConditionResponse)) # Apenas para saber o formato que está vindo
        weatherInfo['textoClima'] = CurrentConditionResponse[0]['WeatherText']
        weatherInfo['temperatura'] = CurrentConditionResponse[0]['Temperature']['Metric']['Value']
        weatherInfo['localName'] = localName
        return weatherInfo

# inicio do programa (execução)

coordinates = getCoordinates()

local = getLocalCode(coordinates['lat'], coordinates['long'])

currentWeather = getCurrentWeather(local['localCode'], local['localName'])

print('Clime atual em: ' + currentWeather['localName'])
print(currentWeather['textoClima'])
print('Temperature: ' + currentWeather['Temperature'] + "\xb0" + "C")

