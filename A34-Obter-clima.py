import requests
import json
import pprint

accuweatherAPIKey = '6ZxEsAOjNyT0h2EnC5rQlW8Brg4tCGtB' # API Key para acessar a api accuWeather

r = requests.get('http://www.geoplugin.net/json.gp') # url da api
if (r.status_code != 200):
    print('Não foi possível obter a localização (r).')
else:
    location = json.loads(r.text) # transformar o request da api em Json
    long = location['geoplugin_longitude'] # acessando a longitude
    lat = location['geoplugin_latitude'] # acessando a latitude
    # print(pprint.pprint(location)) # Para visualizar de forma mais fácil
    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherAPIKey + "&q=" + lat + "%2C" + long + "&language=pt-br" # endereço da pi com a Key, latitude e longitude

    r2 = requests.get(locationAPIUrl) # acessando a api com o key para obter o código do local (key)
    if (r.status_code != 200):
        print('Não foi possível obter a localização (r2).')
    else:
        locationResponse = (json.loads(r2.text)) # transformando o response em json
        nomeLocal = locationResponse['LocalizedName'] + "," + locationResponse['AdministrativeArea']['LocalizedName'] + "." + locationResponse['Country']['LocalizedName']
        codigoLocal = locationResponse['Key']
        print("Obtendo o clima do local: ", nomeLocal)        

        CurrentConditionAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigoLocal + "?apikey=" + accuweatherAPIKey + "&language=pt-br"

        r3 = requests.get(CurrentConditionAPIUrl) # Acessando outra api para obter a temperatura com a chave do local obtido na requisição anterior.
        if (r3.status_code != 200):
            print('Não foi possível obter a localização (r3).')
        else:
            CurrentConditionResponse = (json.loads(r3.text))
            # print(pprint.pprint(CurrentConditionResponse)) # Apenas para saber o formato que está vindo
            textoClima = CurrentConditionResponse[0]['WeatherText']
            temperatura = CurrentConditionResponse[0]['Temperature']['Metric']['Value']
            print('Clima no momento: ' + textoClima)
            print('Temperatura: ' + str(temperatura) + ' graus Celsius')