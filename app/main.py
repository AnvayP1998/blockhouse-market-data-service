from fastapi import FastAPI

app = FastAPI()

@app.get("/prices/latest")
def get_latest_price(symbol: str, provider: str = "yfinance"):
    return {
        "symbol": symbol,
        "price": 123.45,   # dummy value for now
        "timestamp": "2024-01-01T00:00:00Z",
        "provider": provider
    }

@app.post("/prices/poll")
def poll_prices(payload: dict):
    return {
        "job_id": "poll_123",
        "status": "accepted",
        "config": payload
    }
