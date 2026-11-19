from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_analyze():
    response = client.post("/analyze", json={"text": "We need a cloud migration in 3 months, budget $15k", "sender_name": "Ravi"})
    assert response.status_code == 200
    body = response.json()
    assert body["intent"] == "project_inquiry"
    assert body["route_to"]
    assert body["draft_reply"]


def test_validation():
    assert client.post("/analyze", json={"text": ""}).status_code == 422
