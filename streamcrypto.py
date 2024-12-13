from confluent_kafka import Producer
import requests
import json
import time
from pymongo import MongoClient
from datetime import datetime, timezone

# Konfigurasi API
API_URL = "https://api.coincap.io/v2/assets/bitcoin"  # Fokus hanya pada Bitcoin
API_KEY = "14c73165-3aaa-4e59-b456-4b2566321dde"

# Koneksi ke Kafka Producer
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Koneksi ke MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['crypto_database']
collection = db['bitcoin_data']  # Koleksi di MongoDB untuk menyimpan data

def fetch_and_store():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        # Fetch data dari API
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            asset = response.json()['data']
            
            # Format data untuk disimpan
            formatted_data = {
                "Waktu": datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),  # Format waktu UTC
                "Harga Penutupan (USD)": float(asset['priceUsd'])  # Harga penutupan dalam USD
            }
            
            # Simpan ke MongoDB
            inserted = collection.insert_one(formatted_data)
            print(f"Data berhasil disimpan ke MongoDB: {formatted_data}")
            
            # Tambahkan '_id' sebagai string untuk Kafka
            formatted_data['_id'] = str(inserted.inserted_id)
            
            # Kirim ke Kafka
            producer.produce('crypto-topic', value=json.dumps(formatted_data))
            producer.flush()
            print(f"Data dikirim ke Kafka: {formatted_data}")
        else:
            print(f"Error fetching data: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Loop untuk menarik data setiap 10 menit
while True:
    fetch_and_store()
    time.sleep(600)  # Tunggu 10 menit sebelum menarik data lagi
