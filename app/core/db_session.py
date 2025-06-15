from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Gotu%402305%40%23%29%25@localhost:5432/marketdata"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
