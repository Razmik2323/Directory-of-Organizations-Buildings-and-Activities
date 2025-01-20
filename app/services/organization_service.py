from sqlalchemy.orm import Session
from app.models.organization import Organization, OrganizationActivity
from app.schemas.organization import OrganizationCreate


class OrganizationService:

    def __init__(self, db: Session):
        self.db = db

    def create_organization(self, organization_data: OrganizationCreate) -> Organization:
        """Создает новую организацию в базе данных."""
        new_organization = Organization(**organization_data.model_dump(exclude={"activity_ids"}))
        self.db.add(new_organization)
        self.db.commit()
        self.db.refresh(new_organization)
        return new_organization

    def get_all_organizations(self) -> list[Organization]:
        """Возвращает список всех организаций из базы данных."""
        return self.db.query(Organization).all()
