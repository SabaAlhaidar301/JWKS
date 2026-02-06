from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_jwks_only_active_key():
    response = client.get("/.well-known/jwks.json")
    body = response.json()

    kids = [k["kid"] for k in body["keys"]]

    assert "active-key" in kids
    assert "expired-key" not in kids
