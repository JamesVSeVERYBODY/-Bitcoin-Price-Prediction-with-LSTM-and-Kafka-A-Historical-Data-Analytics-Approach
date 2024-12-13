# Bitcoin-Price-Prediction-with-LSTM-and-Kafka-A-Historical-Data-Analytics-Approach
This project focuses on predicting Bitcoin prices using a Long Short-Term Memory (LSTM) neural network based on historical price data. The system integrates Apache Kafka for real-time data streaming and MongoDB for data storage, providing a robust pipeline for data collection, processing, and analysis.

Features
Real-time Data Streaming: Fetches Bitcoin price data every 10 minutes using the CoinCap API and streams it through Kafka.
Data Storage: Stores historical Bitcoin price data in MongoDB for further analysis and model training.
LSTM Model: Implements an LSTM neural network to predict Bitcoin prices based on historical data.
Scalable Architecture: Leverages Kafka’s distributed nature to handle real-time data efficiently.
Flexible Predictions: Provides accurate price predictions for the next day based on learned historical patterns.
Technologies Used
Apache Kafka: For real-time data streaming.
MongoDB: As a NoSQL database for data storage.
Python: For API integration, data processing, and model training.
LSTM: Neural network architecture for time series forecasting.
