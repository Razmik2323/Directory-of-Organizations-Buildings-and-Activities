from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_building():
    response = client.post("/api/v1/buildings/", json={
        "address": "123 Test St",
        "latitude": 40.7128,
        "longitude": -74.0060,
    })
    assert response.status_code == 200
    assert response.json()["address"] == "123 Test St"

def test_list_buildings():
    response = client.get("/api/v1/buildings/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
