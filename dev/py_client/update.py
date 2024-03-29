import requests
from getpass import getpass

user = input('Enter username: ')
password = getpass('Enter password: ')
token_endpoint = 'http://localhost:8000/api/auth/'
token = requests.post(token_endpoint, json={'username': user, 'password': password})
print(token.json())


headers = {"Authorization": f"Token {token.json()['token']}"}

endpoint = 'http://localhost:8000/api/products/2/update/'

data = {
    'title': 'updated title',
}

response = requests.put(endpoint, json=data, headers=headers)
print(response.status_code)