
def fetch_price(crypto_id):
    print(f"Simulating fetch from CoinGecko for {crypto_id}")
    return {"crypto_id": crypto_id, "price": 1000}

def fetch_historical(crypto_id):
    print(f"Simulating fetch historical data from CoinGecko for {crypto_id}")
    return {"crypto_id": crypto_id, "historical": "Sample historical data"}