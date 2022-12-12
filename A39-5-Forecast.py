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

def getLocalCode(lat, long):
    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + apiKey + "&q=" + lat + "%2C" + long + "&language=pt-br"
    r = requests.get(locationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a localização (localCode)')
        return None
    else:
        try:
            localCodeResponse = (json.loads(r.text))
            # print(pprint.pprint(localCodeResponse))
            localInfo = {}
            localInfo['localName'] = localCodeResponse['LocalizedName'] + " , " + localCodeResponse['AdministrativeArea']['LocalizedName'] + " - " + localCodeResponse['Country']['LocalizedName']
            localInfo['localCode'] = localCodeResponse['Key']
            print(localInfo)
            return localInfo
        except:
            return None

def getWeatherForecast(localCode, localName):
    weatherForecast = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + localCode + "?apikey=" + apiKey + "&language=pt-br&metric=true"
    r = requests.get(weatherForecast)
    if (r.status_code != 200):
        print('Não foi possível obter a previsão do tempo, tente novamente.')
        return None
    else:
        try:
            forecastResponse = (json.loads(r.text))
            # forecast = forecastResponse[DailyForecasts]
            # print(pprint.pprint(forecastResponse))
            # detailed = forecastResponse['DailyForecast']
            weatherInfo = []
            for item in forecastResponse['DailyForecasts']:
                print(item)
                weatherInfo['previsao'] = forecastResponse['DailyForecasts']['Temperature']
            return  
        except:
            return None

coordinates = getCoordinates()
local = getLocalCode(coordinates['lat'], coordinates['long'])
forecast = getWeatherForecast(local['localCode'], local['localName'])