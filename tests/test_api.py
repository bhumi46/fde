from fastapi.testclient import TestClient

from acme.api import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_list_shipments():
    response = client.get("/shipments", params={"limit": 3})
    assert response.status_code == 200
    assert len(response.json()) == 3


# --- Phase 3 exercises ----------------------------------------------------

def test_late_shipments_endpoint():
    response = client.get("/shipments/late", params={"as_of": "2026-10-10"})
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 8
    assert all("days_late" in s for s in body)


def test_late_shipments_filter_by_carrier():
    response = client.get(
        "/shipments/late", params={"as_of": "2026-10-10", "carrier": "FastFreight"}
    )
    assert response.status_code == 200
    assert {s["shipment_id"] for s in response.json()} == {"SH-1002", "SH-1011"}
