import requests

URL = 'https://randomuser.me/api/'

count = int(input('Ingresa la cantidad de usuarios: '))
response = requests.get(URL, params={'results': count})

if response.status_code == 200:
    payload = response.json()
    results = payload.get('results')

    for user in results:
        name = user.get('name') #dict

        print("{title} {first} {last}".format(**name))