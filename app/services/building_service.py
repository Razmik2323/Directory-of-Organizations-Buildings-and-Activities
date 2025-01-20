from sqlalchemy.orm import Session
from app.models.building import Building
from app.schemas.building import BuildingCreate


class BuildingService:

    def __init__(self, db: Session):
        self.db = db

    def create_building(self, building_data: BuildingCreate) -> Building:
        """Создает новое здание в базе данных."""
        new_building = Building(**building_data.model_dump())
        self.db.add(new_building)
        self.db.commit()
        self.db.refresh(new_building)
        return new_building

    def get_all_buildings(self) -> list[Building]:
        """Возвращает список всех зданий из базы данных."""
        return self.db.query(Building).all()
