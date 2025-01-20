from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_organization():
    response = client.post("/api/v1/organizations/", json={
        "name": "Test Organization",
        "phone_numbers": "123-456-7890",
        "building_id": 1,
        "activity_ids": []
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Organization"

def test_list_organizations():
    response = client.get("/api/v1/organizations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
