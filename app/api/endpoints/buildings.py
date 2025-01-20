from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.building import BuildingCreate, Building
from app.services.building_service import BuildingService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/buildings/", response_model=Building)
def create_building(building_data: BuildingCreate, db: Session = Depends(get_db)):
    service = BuildingService(db)
    return service.create_building(building_data)


@router.get("/buildings/", response_model=list[Building])
def list_buildings(db: Session = Depends(get_db)):
    service = BuildingService(db)
    return service.get_all_buildings()
