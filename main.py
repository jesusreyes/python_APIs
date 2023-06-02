import requests
from settings import *

"""
    
code = '33ccf8d1d38fcd2d584a'

URL = 'https://github.com/login/oauth/access_token'

params = {
    'client_id': CLIENT_ID,
    'client_secret': SECRET_ID,
    'code': code
}

headers = {
    'Accept': 'application/json'
}

response = requests.post(URL, params=params, headers=headers)

if response.status_code == 200:
    print(response.json())
    print(response.url)

"""

URL = 'https://api.github.com/user'


headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(URL, headers=headers)

print(response.status_code)
print(response.text)






