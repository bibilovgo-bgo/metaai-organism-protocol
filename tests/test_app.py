"""HTTP-layer smoke test: the FastAPI demo serves the full flow + dashboard."""

from fastapi.testclient import TestClient

from src.metaai_core.app import app

client = TestClient(app)


def test_healthz():
    assert client.get("/healthz").json()["status"] == "ok"


def test_full_http_flow_and_dashboard():
    assert client.post("/tick").json()["ok"] is True
    decisions = client.get("/decisions").json()
    assert decisions and decisions[0]["status"] == "pending"

    did = decisions[0]["id"]
    assert client.post(f"/decisions/{did}/approve").json()["status"] == "approved"

    events = client.get("/events").json()
    assert any(e["type"] == "action.executed" for e in events)

    assert client.get("/").status_code == 200  # dashboard renders
