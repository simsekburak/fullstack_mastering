import pytest
from flask import Flask

def create_minimal_app() -> Flask:
    app = Flask(__name__)
    app.config["TESTING"] = True  # Test modunda ayrıntılı hata yakalama

    @app.get("/health")
    def health():
        # Uygulamanın canlı olduğunu göstermek için en basit kontrol
        return {"status": "ok"}, 200

    return app

@pytest.fixture
def client():
    app = create_minimal_app()
    return app.test_client()  # Flask test client, HTTP isteklerini simüle eder

def test_health_ok(client):
    resp = client.get("/health")  # Health endpoint'ini çağır
    assert resp.status_code == 200  # 200 dönmeli
    assert resp.get_json() == {"status": "ok"}  # JSON içeriğini doğrula