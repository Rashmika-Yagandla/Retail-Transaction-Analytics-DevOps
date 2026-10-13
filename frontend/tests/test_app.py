from app import app

def test_dashboard_loads():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Retail Transaction Analytics" in response.data

def test_frontend_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
