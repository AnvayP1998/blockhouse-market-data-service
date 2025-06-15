import app.services.kafka_producer
from app.services.market_data import fetch_and_save_price
from fastapi import FastAPI
from app.services.market_data import fetch_price_with_cache
from pydantic import BaseModel
from app.models.models import PollingJob
from app.core.db_session import SessionLocal
from app.api import prices
app.include_router(prices.router)

app = FastAPI()
class PollRequest(BaseModel):
    symbol: str
    provider: str = "yfinance"
    interval_minutes: int

@app.get("/prices/latest")
def get_latest_price(symbol: str, provider: str = "yfinance"):
    result = fetch_price_with_cache(symbol, provider)
    return result


@app.post("/prices/poll")
def poll_prices(req: PollRequest):
    db = SessionLocal()
    job = PollingJob(
        symbol=req.symbol,
        provider=req.provider,
        interval_minutes=req.interval_minutes
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    db.close()
    return {
        "job_id": job.id,
        "status": "scheduled",
        "symbol": req.symbol,
        "interval_minutes": req.interval_minutes
    }
