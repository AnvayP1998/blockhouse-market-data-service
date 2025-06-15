from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Column, Integer, String, DateTime
import datetime
from sqlalchemy import Float


Base = declarative_base()

class RawMarketData(Base):
    __tablename__ = 'raw_market_data'
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    provider = Column(String)

class MovingAverage(Base):
    __tablename__ = 'moving_averages'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, index=True)
    avg_price = Column(Float)
    window_size = Column(Integer)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class PollingJob(Base):
    __tablename__ = 'polling_jobs'
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    provider = Column(String)
    interval_minutes = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)