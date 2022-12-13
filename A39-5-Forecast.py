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
            # print(coordinate['long'])
            # print(coordinate['lat'])
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
            # print(localInfo)
            return localInfo
        except:
            return None

def getCurrentWeather(localCode, localName):

    CurrentConditionAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + localCode + "?apikey=" + apiKey + "&language=pt-br"

    r = requests.get(CurrentConditionAPIUrl) # Acessando outra api para obter a temperatura com a chave do local obtido na requisição anterior.
    if (r.status_code != 200):
        print('Não foi possível obter o clima atual (r3).')
        return None
    else:
        try:
            CurrentConditionResponse = (json.loads(r.text))
            weatherInfo = {}
            # print(pprint.pprint(CurrentConditionResponse)) # Apenas para saber o formato que está vindo
            weatherInfo['textoClima'] = CurrentConditionResponse[0]['WeatherText']
            weatherInfo['temperatura'] = CurrentConditionResponse[0]['Temperature']['Metric']['Value']
            weatherInfo['localName'] = localName
            return weatherInfo
        except:
            return None

def getWeatherForecast(localCode):
    weatherForecast = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + localCode + "?apikey=" + apiKey + "&language=pt-br&metric=true"
    r = requests.get(weatherForecast)
    if (r.status_code != 200):
        print('Não foi possível obter a previsão do tempo, tente novamente.')
        return None
    else:
        try:
            forecastResponse = (json.loads(r.text))
            weatherInfo = []
            for item in forecastResponse['DailyForecasts']:
                forecast = {}
                # print(item)
                forecast['clima'] = item['Day']['IconPhrase']
                forecast['max'] = item['Temperature']['Maximum']['Value']
                forecast['min'] = item['Temperature']['Minimum']['Value']
                forecast['dia'] = item['EpochDate']
                weatherInfo.append(forecast)
                # print(weatherInfo)
            return  weatherInfo
        except:
            return None
try:
    coordinates = getCoordinates()
    local = getLocalCode(coordinates['lat'], coordinates['long'])
    currentWeather = getCurrentWeather(local['localCode'], local['localName'])

    print('Clima atual em: ', local['localName'])
    print('Clima: ',currentWeather['textoClima'])

    forecast = getWeatherForecast(local['localCode'])
    print(forecast['clima'], forecast['max'], forecast['min'], forecast['dia'])
    for day in forecast:
        print(day['dia'])
        print('Mínima: ' + str(day['min']) + "\xb0" + "C")
        print('Máxima: ' + str(day['max']) + "\xb0" + "C")
        print('Clima: ' + day['clima'])

except:
    print('Erro  ao processar a solicitação. Entre em contato com o suporte.')