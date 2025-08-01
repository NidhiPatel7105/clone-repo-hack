# test_main.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_token_protected():
    response = client.get("/")
    assert response.status_code == 403 or response.status_code == 401
