import requests

URL = 'http://httpbin.org/get'

response = requests.get(URL) #GET
print(response)
print(response.status_code)
print(response.text)

payload = response.json()
print(payload.get('origin')) ## Transforma respuesta en dict

print(response.url)
