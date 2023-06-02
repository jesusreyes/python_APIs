import requests

## Opcion Request 1
URL = 'https://httpbin.org/get'
URL_with_query = URL + '?name=jesus&password=123&email=mail@gmail.com'

response = requests.get(URL_with_query) #GET

if response.status_code == 200:
    payload = response.json()
    params = payload['args']

    print(params['name'])
    print(params['password'])
    print(params['email'])

## Opcion Request 2

params = {
    'name': 'jesus',
    'password': '123',
    'email': 'mail@gmail.com'
}

response = requests.get(URL, params=params) #GET

if response.status_code == 200:
    payload = response.json()
    params = payload['args']

    print(params['name'])
    print(params['password'])
    print(params['email'])

print(response.url)