from fastapi import FastAPI
from app.api.endpoints.buildings import router as buildings_router
from app.api.endpoints.organizations import router as organizations_router
from app.api.endpoints.activities import router as activities_router
from app.database import engine
from app.models.organization import Base as OrgBase
from app.models.building import Base as BldBase
from app.models.activity import Base as ActBase

app = FastAPI()

# Создание таблиц в базе данных SQLite
OrgBase.metadata.create_all(bind=engine)  # Создание таблиц для организаций
BldBase.metadata.create_all(bind=engine)  # Создание таблиц для зданий
ActBase.metadata.create_all(bind=engine)  # Создание таблиц для видов деятельности

# Подключение маршрутов
app.include_router(buildings_router, prefix="/api/v1/buildings", tags=["Buildings"])
app.include_router(organizations_router, prefix="/api/v1/organizations", tags=["Organizations"])
app.include_router(activities_router, prefix="/api/v1/activities", tags=["Activities"])


@app.get("/")
def root():
    return {"message": "Welcome to the Organizations Directory API!"}
