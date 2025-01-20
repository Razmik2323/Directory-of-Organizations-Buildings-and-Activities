from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base


class Organization(Base):
    """Модель для представления организации."""
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_numbers = Column(String)  # Номера телефонов в виде строки (можно использовать JSONField)

    building_id = Column(Integer, ForeignKey("buildings.id"))
    building = relationship("Building", back_populates="organizations")

    activities = relationship("OrganizationActivity", back_populates="organization")


class OrganizationActivity(Base):
    """Связующая таблица между организациями и видами деятельности."""
    __tablename__ = "organization_activities"

    organization_id = Column(Integer, ForeignKey("organizations.id"), primary_key=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), primary_key=True)

    organization = relationship("Organization", back_populates="activities")
    activity = relationship("Activity", back_populates="organizations")
