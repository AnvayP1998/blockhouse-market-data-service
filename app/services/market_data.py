import yfinance as yf
from app.models.models import RawMarketData
from app.core.db_session import SessionLocal
import datetime
from sqlalchemy import desc
import datetime
from app.services.kafka_producer import publish_price_event

def fetch_and_save_price(symbol, provider="yfinance"):
    try:
        data = yf.Ticker(symbol)
        price = data.history(period="1d").tail(1)["Close"].values[0]
        price = float(price)  # <-- FIX
        timestamp = datetime.datetime.utcnow()
        db = SessionLocal()
        record = RawMarketData(
            symbol=symbol,
            price=price,
            timestamp=timestamp,
            provider=provider
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        event = {
            "symbol": symbol,
            "price": price,
            "timestamp": timestamp.isoformat(),
            "provider": provider,
            "raw_response_id": str(record.id),
        }
        publish_price_event(event)
        db.close()
        return {"symbol": symbol, "price": price, "timestamp": timestamp.isoformat(), "provider": provider}
    except Exception as e:
        return {"error": str(e)}

def get_latest_price_from_db(symbol, provider="yfinance", max_age_minutes=5):
    db = SessionLocal()
    since = datetime.datetime.utcnow() - datetime.timedelta(minutes=max_age_minutes)
    result = db.query(RawMarketData).filter(
        RawMarketData.symbol == symbol,
        RawMarketData.provider == provider,
        RawMarketData.timestamp >= since
    ).order_by(desc(RawMarketData.timestamp)).first()
    db.close()
    return result

def fetch_price_with_cache(symbol, provider="yfinance", max_age_minutes=5):
    recent = get_latest_price_from_db(symbol, provider, max_age_minutes)
    if recent:
        return {
            "symbol": recent.symbol,
            "price": recent.price,
            "timestamp": recent.timestamp.isoformat(),
            "provider": recent.provider,
            "cached": True
        }
    # If not found/recent, fetch new and save
    return fetch_and_save_price(symbol, provider)
