from pydantic import BaseModel

class ActivityBase(BaseModel):
    """Базовая схема вида деятельности."""
    name: str

class ActivityCreate(ActivityBase):
    """Схема для создания нового вида деятельности."""
    parent_id: int | None

class Activity(ActivityBase):
    """Схема для представления вида деятельности с ID."""
    id: int

    class Config:
        orm_mode = True
