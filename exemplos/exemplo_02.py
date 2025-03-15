import requests

url = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"
parametros = {
    "tickers": "btc-bitcoin",
    "quotes": "USD"
}
response = requests.get(url, params=parametros)

print(response.json())