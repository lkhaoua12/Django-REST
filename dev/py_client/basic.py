import requests

endpoint = "http://localhost:8000/api/"
response = requests.post(endpoint, json={'jkh': 'hello world'})
print(response.json())