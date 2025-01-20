from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Activity(Base):
    """Модель для представления вида деятельности."""
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey("activities.id"), nullable=True)

    children = relationship("Activity", backref="parent", remote_side=[id])
    organizations = relationship("OrganizationActivity", back_populates="activity")
