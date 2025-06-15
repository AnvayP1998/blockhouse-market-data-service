from app.models.models import Base
from sqlalchemy import create_engine

# Use your DOCKER network Postgres host (should match your docker-compose service name)
engine = create_engine("postgresql://postgres:Gotu%402305%40%23%29%25@db:5432/marketdata")

Base.metadata.create_all(engine)
print("Tables created!")
