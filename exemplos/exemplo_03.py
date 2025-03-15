import requests

url = "https://api.coinbase.com/v2/prices/spot"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}
parametros = {
    "currency": "USD"
}
response = requests.get(url, headers=headers, params=parametros)

print(response.json())
