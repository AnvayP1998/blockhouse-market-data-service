from confluent_kafka import Consumer
import json
import time
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from app.models.models import RawMarketData, MovingAverage, Base
import datetime

KAFKA_CONFIG = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'moving-average-calc',
    'auto.offset.reset': 'earliest'
}
print("KAFKA_CONFIG:", KAFKA_CONFIG)

def get_last_n_prices(session, symbol, n=5):
    return session.query(RawMarketData)\
        .filter(RawMarketData.symbol == symbol)\
        .order_by(desc(RawMarketData.timestamp))\
        .limit(n)\
        .all()

def upsert_moving_average(session, symbol, avg, window_size, timestamp):
    existing = session.query(MovingAverage).filter_by(symbol=symbol, timestamp=timestamp).first()
    if existing:
        existing.avg_price = avg
        existing.window_size = window_size
    else:
        ma = MovingAverage(symbol=symbol, avg_price=avg, window_size=window_size, timestamp=timestamp)
        session.add(ma)
    session.commit()

if __name__ == "__main__":
    consumer = Consumer(KAFKA_CONFIG)
    consumer.subscribe(["price-events"])
    engine = create_engine("postgresql://postgres:Gotu%402305%40%23%29%25@db:5432/marketdata")
    Session = sessionmaker(bind=engine)

    print("Listening for price events...")
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Kafka error: {msg.error()}")
            continue
        try:
            event = json.loads(msg.value().decode('utf-8'))
            symbol = event["symbol"]
            timestamp = datetime.datetime.fromisoformat(event["timestamp"])
            session = Session()
            prices = get_last_n_prices(session, symbol, n=5)
            if len(prices) == 5:
                avg = sum([p.price for p in prices]) / 5.0
                upsert_moving_average(session, symbol, avg, 5, timestamp)
                print(f"Moving average for {symbol}: {avg}")
            session.close()
        except Exception as e:
            print(f"Processing error: {e}")
