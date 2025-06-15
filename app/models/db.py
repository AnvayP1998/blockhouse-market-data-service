from sqlalchemy import create_engine
from app.models.models import Base


DATABASE_URL = "postgresql://postgres:Gotu%402305%40%23%29%25@db:5432/marketdata"

engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
