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

               +--------------------+
               |  User / Client     |
               +---------+----------+
                         |
                   REST  |
                         v
      +--------------------------+
      |      FastAPI App         |
      | - /prices/latest         |
      | - /prices/poll           |
      +--------------------------+
          |                 |

(SQLAlchemy) | (Kafka producer)
v v
+----------------+ +------------------+
| PostgreSQL | | Kafka Topic: |
| raw_market_data|<--| price-events |
+----------------+ +------------------+
|
(Kafka consumer)
v
+-------------------------+
| Compute Moving Average |
| Insert into Postgres |
| moving_averages |
+-------------------------+