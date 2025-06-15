from fastapi.testclient import TestClient
from app.main import app

def test_prices_latest():
    client = TestClient(app)
    response = client.get("/prices/latest?symbol=AAPL&provider=yfinance")
    assert response.status_code == 200
    data = response.json()
    assert "symbol" in data
    assert "price" in data
