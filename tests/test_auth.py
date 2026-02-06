from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_valid_jwt():
    response = client.post("/auth")
    assert response.status_code == 200
    assert "." in response.text


def test_expired_jwt():
    response = client.post("/auth?expired=true")
    assert response.status_code == 200
    assert "." in response.text


def test_invalid_method():
    response = client.get("/auth")
    assert response.status_code == 405
