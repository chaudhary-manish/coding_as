from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_app():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome To FastAPI World"}