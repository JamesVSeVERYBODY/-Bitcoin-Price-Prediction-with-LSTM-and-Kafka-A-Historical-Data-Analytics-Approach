Bitcoin Price Prediction Using LSTM Based on Historical Data Analytics with Kafka
This project predicts Bitcoin prices using a Long Short-Term Memory (LSTM) neural network based on historical price data. It integrates Apache Kafka for real-time data streaming and MongoDB for data storage, creating a robust pipeline for data collection, processing, and analysis.

Features
🔄 Real-Time Data Streaming
Fetches Bitcoin price data every 10 minutes using the CoinCap API and streams it through Kafka.

💾 Data Storage
Stores historical Bitcoin price data in MongoDB for further analysis and model training.

📈 LSTM Model for Prediction
Implements an LSTM neural network to predict Bitcoin prices based on historical data.

⚡ Scalable Architecture
Leverages Kafka's distributed nature to handle real-time data efficiently.

🎯 Accurate Predictions
Provides accurate price predictions for the next day based on learned historical patterns.

Technologies Used
Apache Kafka: For real-time data streaming.
MongoDB: NoSQL database for storing and managing Bitcoin price data.
Python: For API integration, data processing, and LSTM model implementation.
LSTM (Long Short-Term Memory): Neural network architecture designed for time series forecasting.
Repository Contents
streamcrypto.py
Script to fetch Bitcoin price data from the CoinCap API and send it to Kafka.

consumercrypto.py
Kafka consumer to process and store Bitcoin price data in MongoDB.

BTC_Forecast.ipynb
Jupyter Notebook for LSTM model training and price prediction.

database.py
Utility script for database management and additional consumer functionality.

How It Works
Data Collection
The system fetches real-time Bitcoin price data from the CoinCap API.

Data Streaming
The fetched data is sent to a Kafka topic for streaming.

Data Storage
Kafka consumer processes the data and stores it in MongoDB for historical tracking.

Prediction
The LSTM model uses historical data from MongoDB to predict Bitcoin prices for the next day.

Getting Started
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/bitcoin-price-prediction.git
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the producer and consumer:
bash
Copy code
python streamcrypto.py
python consumercrypto.py
Train the LSTM model:
bash
Copy code
jupyter notebook BTC_Forecast.ipynb
License
This project is licensed under the MIT License. See the LICENSE file for details.

