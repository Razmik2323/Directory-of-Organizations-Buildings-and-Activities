from pydantic import BaseModel
from typing import List


class OrganizationBase(BaseModel):
    """Базовая схема организации."""
    name: str
    phone_numbers: str


class OrganizationCreate(OrganizationBase):
    """Схема для создания новой организации."""
    building_id: int
    activity_ids: List[int]


class Organization(OrganizationBase):
    """Схема для представления организации с ID."""
    id: int

    class Config:
        orm_mode = True
