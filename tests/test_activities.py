from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_activity():
    response = client.post("/api/v1/activities/", json={
        "name": "Test Activity",
        "parent_id": None,
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Activity"

def test_list_activities():
    response = client.get("/api/v1/activities/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
