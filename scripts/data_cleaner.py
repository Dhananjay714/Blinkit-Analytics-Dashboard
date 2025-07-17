import requests
import pandas as pd
from time import sleep
import os

# Path to CSV file
csv_file = "../data/orders_data.csv"

# Create CSV file with headers if it doesn't exist
if not os.path.exists(csv_file):
    df_header = pd.DataFrame(columns=[
        'order_id', 'product', 'price', 'quantity', 'city',
        'order_time', 'payment_method', 'delivery_time_min', 'total_price'
    ])
    df_header.to_csv(csv_file, index=False)

# Infinite loop to fetch API data every 5 seconds
while True:
    try:
        response = requests.get("http://localhost:5000/orders")
        data = response.json()

        # Convert to DataFrame
        df = pd.DataFrame(data)
        df['order_time'] = pd.to_datetime(df['order_time'])
        df['total_price'] = df['price'] * df['quantity']

        # Append to CSV without header
        df.to_csv(csv_file, mode='a', index=False, header=False)

        print(f"{len(df)} new records added to orders_data.csv")

        sleep(5)  # wait for 5 seconds before next fetch

    except Exception as e:
        print("Error occurred:", e)
        sleep(5)
