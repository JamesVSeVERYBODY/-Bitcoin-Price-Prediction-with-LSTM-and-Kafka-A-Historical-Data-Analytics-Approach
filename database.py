from confluent_kafka import Consumer
from pymongo import MongoClient
import json

# Konfigurasi Kafka Consumer
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'crypto-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)
consumer.subscribe(['crypto-topic'])

# Koneksi ke MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['crypto_database']
collection = db['crypto_data']

print("Listening to Kafka topic and storing data in MongoDB...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    # Decode pesan dari Kafka
    data = json.loads(msg.value().decode('utf-8'))
    print(f"Received data: {data}")

    # Simpan ke MongoDB
    collection.insert_one(data)

consumer.close()
