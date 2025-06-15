from fastapi import APIRouter, BackgroundTasks
from app.models.models import PollingJobConfig
from app.core.db_session import SessionLocal
import datetime

router = APIRouter()

@router.post("/prices/poll")
def create_polling_job(body: dict, background_tasks: BackgroundTasks):
    symbols = body.get("symbols")
    interval = body.get("interval", 60)
    provider = body.get("provider", "yfinance")

    db = SessionLocal()
    job = PollingJobConfig(
        symbols=symbols,
        interval=interval,
        provider=provider,
        status="active",
        created_at=datetime.datetime.utcnow()
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    db.close()

    # (Optional: Launch background polling here, for now just stub)
    return {
        "job_id": job.id,
        "symbols": symbols,
        "interval": interval,
        "provider": provider,
        "status": "active"
    }
