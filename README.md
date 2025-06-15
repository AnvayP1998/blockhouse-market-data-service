# Blockhouse Market Data Service

A production-style market data microservice for Blockhouse Capital. Built with FastAPI, PostgreSQL, Kafka, Docker, and Python. Supports price fetching, polling, event streaming, and moving average computation.

---

## Features
- Fetch real-time price data from external providers (e.g. yfinance)
- Poll prices on a schedule
- Event-driven data pipeline via Kafka
- Compute and store moving averages
- Production-style project structure and Dockerization

## Tech Stack
- Python 3.10+
- FastAPI
- PostgreSQL
- Kafka & Zookeeper
- Docker Compose

## Architecture Diagram

    +--------------+        REST API         +-------------------+
    | User/Client  | <-------------------->  |  FastAPI Service  |
    +--------------+                        | /prices/latest     |
                                            | /prices/poll       |
                                            +-------------------+
                                                    |
                                  +-----------------+------------------+
                         (SQLAlchemy)              |      Kafka Producer
                                                    v
                      +-------------------+   +------------------------+
                      |   PostgreSQL      |   |  Kafka: price-events   |
                      | raw_market_data   |<--|  (topic for events)    |
                      +-------------------+   +------------------------+
                                                     |
                                                Kafka Consumer
                                                     v
                                     +-----------------------------+
                                     | Compute Moving Average      |
                                     | Insert into moving_averages |
                                     +-----------------------------+
## Setup Instructions
1) Clone the repository:
git clone https://github.com/<your-username>/blockhouse-market-data-service.git
cd blockhouse-market-data-service
2) Create and activate a virtual environment:
python -m venv venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
3) Install Python dependencies:
pip install -r requirements.txt
4) Start all services with Docker Compose:
docker compose up -d
5) Initialize the database:
python -m app.models.db
6) Run the FastAPI application:
uvicorn app.main:app --reload
- Visit http://127.0.0.1:8000/docs for Swagger API docs.
7) Run the Kafka consumer (in a new terminal):
python -m scripts.kafka_consumer


