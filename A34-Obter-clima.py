import requests
import json
import pprint

accuwweatherAPIKey = '6ZxEsAOjNyT0h2EnC5rQlW8Brg4tCGtB'

r = requests.get('http://www.geoplugin.net/json.gp')
if (r.status_code != 200):
    print('Não foi possível obter a localização (r).')
else:
    location = json.loads(r.text)
    long = location['geoplugin_longitude']
    lat = location['geoplugin_latitude']
    # print(pprint.pprint(location)) # Para visualizar de forma mais fácil
    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuwweatherAPIKey + "&q=" + lat + "%2C" + long + "&language=pt-br"

    r2 = requests.get(locationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a localização (r2).')
    else:
        locationResponse = (json.loads(r2.text))
        nomeLocal = locationResponse['LocalizedName'] + "," + locationResponse['AdministrativeArea']['LocalizedName'] + "." + locationResponse['Country']['LocalizedName']
        codigoLocal = locationResponse['Key']
        print("Obtendo o clima do local: ", nomeLocal)
        

        CurrentConditionAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigoLocal + "?apikey=" + accuwweatherAPIKey + "&language=pt-br"

        r3 = requests.get(CurrentConditionAPIUrl)
        if (r3.status_code != 200):
            print('Não foi possível obter a localização (r3).')
        else:
            CurrentConditionResponse = (json.loads(r3.text))
            # print(pprint.pprint(CurrentConditionResponse)) # Apenas para saber o formato que está vindo
            textoClima = CurrentConditionResponse[0]['WeatherText']
            temperatura = CurrentConditionResponse[0]['Temperature']['Metric']['Value']
            print('Clima no momento: ' + textoClima)
            print('Temperatura: ' + str(temperatura) + ' graus Celsius')