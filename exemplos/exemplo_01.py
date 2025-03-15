import requests

url = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"

response = requests.get(url)

print(response.json())
