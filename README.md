# Bitcoin Price Prediction Using LSTM Based on Historical Data Analytics with Kafka

This project predicts Bitcoin prices using a **Long Short-Term Memory (LSTM)** neural network based on historical price data. It integrates **Apache Kafka** for real-time data streaming and **MongoDB** for data storage, creating a robust pipeline for data collection, processing, and analysis.

---

## Features
- 🔄 **Real-Time Data Streaming**  
   Fetches Bitcoin price data every 10 minutes using the CoinCap API and streams it through Kafka.

- 💾 **Data Storage**  
   Stores historical Bitcoin price data in MongoDB for further analysis and model training.

- 📈 **LSTM Model for Prediction**  
   Implements an LSTM neural network to predict Bitcoin prices based on historical data.

- ⚡ **Scalable Architecture**  
   Leverages Kafka's distributed nature to handle real-time data efficiently.

- 🎯 **Accurate Predictions**  
   Provides accurate price predictions for the next day based on learned historical patterns.

---

## Technologies Used
- **Apache Kafka**: For real-time data streaming.
- **MongoDB**: NoSQL database for storing and managing Bitcoin price data.
- **Python**: For API integration, data processing, and LSTM model implementation.
- **LSTM (Long Short-Term Memory)**: Neural network architecture designed for time series forecasting.

---

## Repository Contents
- `streamcrypto.py`  
   Script to fetch Bitcoin price data from the CoinCap API and send it to Kafka.
   
- `consumercrypto.py`  
   Kafka consumer to process and store Bitcoin price data in MongoDB.

- `BTC_Forecast.ipynb`  
   Jupyter Notebook for LSTM model training and price prediction.

- `database.py`  
   Utility script for database management and additional consumer functionality.

---

## How It Works
1. **Data Collection**  
   Fetches real-time Bitcoin price data from the CoinCap API.

2. **Data Streaming**  
   Sends the fetched data to a Kafka topic for streaming.

3. **Data Storage**  
   Kafka consumer processes the data and stores it in MongoDB for historical tracking.

4. **Prediction**  
   Uses historical data from MongoDB to train an LSTM model for predicting Bitcoin prices.

---

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bitcoin-price-prediction.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the producer and consumer:
   ```bash
   python streamcrypto.py
   python consumercrypto.py
4. Train the LSTM Model
  ```bash
   jupyter notebook BTC_Forecast.ipynb
