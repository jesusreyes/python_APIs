import requests

URL = 'https://httpbin.org/post'

# Se puede enviar datos por:
# Query -> GET
# Cuerpo de petición -> POST
# Encabezado

data = {
    'username': 'jesus',
    'password': '1234'
}

headers = {
    'course': 'Curso python',
    'version': '2.0'
}

params = {
    'name': 'jesus reyes',
    'password': '123',
    'email': 'mail@gmail.com'
}

response = requests.post(URL, headers=headers, params=params, data=data)

if response.status_code == 200:
    print(response.text)