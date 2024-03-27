import requests

endpoint = 'http://localhost:8000/api/products/2/update/'

data = {
    'title': 'updated title',
}

response = requests.put(endpoint, json=data)
print(response.status_code)