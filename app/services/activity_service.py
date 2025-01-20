from sqlalchemy.orm import Session
from app.models.activity import Activity
from app.schemas.activity import ActivityCreate


class ActivityService:

    def __init__(self, db: Session):
        self.db = db

    def create_activity(self, activity_data: ActivityCreate) -> Activity:
        """Создает новый вид деятельности в базе данных."""
        new_activity = Activity(**activity_data.model_dump())
        self.db.add(new_activity)
        self.db.commit()
        self.db.refresh(new_activity)
        return new_activity

    def get_all_activities(self) -> list[Activity]:
        """Возвращает список всех видов деятельности из базы данных."""
        return self.db.query(Activity).all()
