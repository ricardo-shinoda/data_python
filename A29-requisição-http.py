import requests
r = requests.get('https://www.google.com')
print(r.status_code) # para printar o status da requisição
print(r.headers)
print(r.headers['Date']) # para saber a data da requisição
print(r.text)