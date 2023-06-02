import requests
from getpass import getpass

URL = 'http://httpbin.org/basic-auth/blue/123'

password = getpass('Ingresa la contraseña: ')

session = requests.session()
session.auth = ('blue', password)

response = session.get(URL)

if response.status_code == 200:
    print(response.json())
    print('Successful authentication.')

if response.status_code == 401:
    print('Unsuccessful authentication.')