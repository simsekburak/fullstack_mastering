import pytest
from flask import Flask

from app import create_app
# create_app: Uygulama fabrikası.
# Ortam bazlı config yüklenmesi, health endpoint'inin tanımlanması ve Flask app örneğinin oluşturulması burada yapılır.


@pytest.fixture
def app() -> Flask:
    """
    Testler için Flask uygulama örneği oluşturan fixture.
    TestingConfig kullanılarak test ortamına uygun ayarlar yüklenir.
    """
    # create_app fonksiyonu 'testing' config adı ile çağrılır.
    # Böylece TestingConfig sınıfındaki TESTING=True, test veritabanı URI'si vb. ayarlar devreye girer.
    app = create_app(config_name="testing")
    return app


@pytest.fixture
def client(app: Flask):
    """
    HTTP isteklerini simüle etmek için Flask test client oluşturan fixture.
    Gerçek bir HTTP sunucusu ayağa kaldırılmadan istek/cevap döngüsü test edilir.
    """
    # app.test_client() ile Flask'ın yerleşik test client'ı üretilir.
    # Bu client üzerinden GET/POST gibi HTTP metodları doğrudan çağrılabilir.
    return app.test_client()


def test_health_ok(client):
    """
    /health endpoint'inin doğru HTTP durum kodu ve beklenen JSON içeriği ile cevap verdiğini doğrulayan test.
    """
    # /health endpoint'ine GET isteği gönderilir.
    resp = client.get("/health")

    # Dönen HTTP durum kodunun 200 (OK) olması beklenir.
    assert resp.status_code == 200

    # Cevap gövdesi JSON olarak parse edilir.
    data = resp.get_json()

    # JSON parse işleminin başarılı olması ve None dönmemesi beklenir.
    assert data is not None

    # 'status' alanının 'ok' değerine sahip olması beklenir.
    assert data.get("status") == "ok"

    # 'env' alanının bilinen ortamlardan biri olması beklenir.
    # Bu alan, create_app içinde kullanılan config ortamını (development/testing/production) yansıtır.
    assert data.get("env") in {"development", "testing", "production"}