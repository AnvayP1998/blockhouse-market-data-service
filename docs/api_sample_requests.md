# Blockhouse Market Data Microservice

## API Sample Requests & Responses

---

### 1. GET /prices/latest

**Request:**

**Sample Response:**
```json
{
  "symbol": "AAPL",
  "price": 196.45,
  "timestamp": "2025-06-15T20:30:27.283671",
  "provider": "yfinance"
}

### 2. POST /prices/poll
Content-Type: application/json

{
  "symbol": "AAPL",
  "interval_minutes": 60,
  "provider": "yfinance"
}
{
  "message": "Polling job scheduled for symbol: AAPL"
}

### Kafka event Ex:
{
  "symbol": "AAPL",
  "price": 196.45,
  "timestamp": "2025-06-15T20:30:27.283671",
  "provider": "yfinance",
  "raw_response_id": "1"
}
