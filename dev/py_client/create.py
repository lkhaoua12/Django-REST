import requests
from getpass import getpass

user = input('Enter username: ')
password = getpass('Enter password: ')
token_endpoint = 'http://localhost:8000/api/auth/'
token = requests.post(token_endpoint, json={'username': user, 'password': password})
print(token.json())


headers = {"Authorization": f"Token {token.json()['token']}"}

endpoint = 'http://localhost:8000/api/products/'
data = {
    'title': 'tested using token auth',
}
response = requests.post(endpoint, json=data, headers=headers)
print(response.json())