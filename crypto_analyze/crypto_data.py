import requests

def get_top_cryptos(n=20):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": n, "page": 1}
    response = requests.get(url, params=params)
    cryptos = [coin["name"] for coin in response.json()]
    return cryptos
