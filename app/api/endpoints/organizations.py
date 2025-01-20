from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.organization import OrganizationCreate, Organization
from app.services.organization_service import OrganizationService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Organization)
def create_organization(organization_data: OrganizationCreate, db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return service.create_organization(organization_data)


@router.get("/", response_model=list[Organization])
def list_organizations(db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return service.get_all_organizations()
