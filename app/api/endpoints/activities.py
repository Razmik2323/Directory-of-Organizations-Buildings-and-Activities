from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.activity import ActivityCreate, Activity
from app.services.activity_service import ActivityService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Activity)
def create_activity(activity_data: ActivityCreate, db: Session = Depends(get_db)):
    service = ActivityService(db)
    return service.create_activity(activity_data)


@router.get("/", response_model=list[Activity])
def list_activities(db: Session = Depends(get_db)):
    service = ActivityService(db)
    return service.get_all_activities()
