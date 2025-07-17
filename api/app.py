from flask import Flask, jsonify
from faker import Faker
import random
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Initialize Faker
fake = Faker()

# List of Indian cities
indian_cities = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad",
    "Pune", "Chennai", "Kolkata", "Jaipur", "Surat", "Lucknow",
    "Nagpur", "Bhopal", "Patna", "Indore", "Thane", "Vadodara"
]

# Function to generate a single fake order
def generate_order():
    return {
        "order_id": fake.uuid4(),
        "product": random.choice(["Paneer", "Milk", "Maggi", "Biscuits", "Eggs", "Bread", "Juice"]),
        "price": round(random.uniform(20, 500), 2),
        "quantity": random.randint(1, 5),
        "city": random.choice(indian_cities),
        "order_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "payment_method": random.choice(["UPI", "Card", "Cash"]),
        "delivery_time_min": random.randint(5, 60)
    }

# API endpoint to return multiple orders
@app.route('/orders')
def get_orders():
    orders = [generate_order() for _ in range(10)]  # 10 orders per request
    return jsonify(orders)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
