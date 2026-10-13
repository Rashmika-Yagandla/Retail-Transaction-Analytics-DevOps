from app import app

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_metrics_shape():
    response = app.test_client().get("/metrics")
    assert response.status_code == 200
    assert response.json["revenue"] > 0
    assert response.json["orders"] > 0

def test_products_endpoint():
    response = app.test_client().get("/products")
    assert response.status_code == 200
    assert len(response.json) >= 1
    assert {"name", "units", "revenue"} <= response.json[0].keys()
