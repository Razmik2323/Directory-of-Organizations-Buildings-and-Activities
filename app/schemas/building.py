from pydantic import BaseModel

class BuildingBase(BaseModel):
    """Базовая схема здания."""
    address: str
    latitude: float
    longitude: float

class BuildingCreate(BuildingBase):
    """Схема для создания нового здания."""
    pass

class Building(BuildingBase):
    """Схема для представления здания с ID."""
    id: int

    class Config:
        orm_mode = True
