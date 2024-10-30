from flask import Blueprint, jsonify
from .services import fetch_price, fetch_historical
from .database import save_to_db
from .models import PriceData

main = Blueprint('main', __name__)

# Fetch price with coin id
@main.route('/price/<crypto_id>')
def get_price(crypto_id):
    print(f"Fetching price for {crypto_id}")
    data = fetch_price(crypto_id)
    
    price_data = PriceData(time="2024-10-01T12:00:00Z", price_usd=data["price"])
    return jsonify({"crypto_id": crypto_id, "timestamp": price_data.time, "price": price_data.price_usd})

# Fetch price with coin id
@main.route('/historical/<crypto_id>')
def get_historical(crypto_id):
    print(f"Fetching historical data for {crypto_id}")
    historical_data = fetch_historical(crypto_id)
    
    return jsonify(historical_data)

# Save data to postgres
@main.route('/save/<crypto_id>')
def save_data(crypto_id):
    print(f"Saving data for {crypto_id}")
    
    data = fetch_price(crypto_id)
    price_data = PriceData(time="2024-10-01T12:00:00Z", price_usd=data["price"])
    
    save_to_db(price_data)
    
    return jsonify({"status": "success", "message": f"Saved data for {crypto_id}"})
