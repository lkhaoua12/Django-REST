import requests

endpoint = 'http://localhost:8000/api/products/'
data = {
    'title': 'new product',
}
response = requests.post(endpoint, json=data)
print(response.json())