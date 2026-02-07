from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_modes_endpoint():
    response = client.get("/modes")
    assert response.status_code == 200
    assert response.json() == {"valid_modes": ["dev", "prod"]}

def test_run_invalid_mode_returns_400():
    response = client.get("/run/test")
    assert response.status_code == 400
    assert response.json() == {"detail": "Unknown mode: test"}