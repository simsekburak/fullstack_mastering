import os
from flask import Flask, jsonify

from config.settings import config
# config: Ortam adına göre (development/testing/production) uygun config sınıfını tutan sözlük
from extensions import db, migrate, cache, limiter, jwt, metrics
# db: SQLAlchemy veritabanı extension'ı
# migrate: Alembic tabanlı migration extension'ı
# cache: Basit cache iskeleti (ileride Redis tabanlı hale getirilebilir)
# limiter: Rate limiting extension'ı
# jwt: JWT tabanlı kimlik doğrulama extension'ı
# metrics: Prometheus metrik sarmalayıcısı

def create_app(config_name: str | None = None) -> Flask:
    """
    Flask uygulamasını oluşturan fabrika fonksiyonu.
    Büyük projelerde tek bir global app yerine, ihtiyaç oldukça app üretilmesi için kullanılır.
    """
    app = Flask(__name__)
    # Yeni bir Flask uygulaması örneği oluşturulur.
    # __name__ değeri, Flask tarafından template ve static dosya yolları gibi amaçlarla kullanılır.

    if config_name is None:
        # Fonksiyon çağrısında özel bir config adı verilmemişse bu blok çalışır.
        # Ortam değişkenlerinden FLASK_ENV değeri okunur; yoksa 'development' varsayılan olarak kullanılır.
        config_name = os.getenv("FLASK_ENV", "development")

    # Seçilen ortama göre uygun config sınıfı belirlenir.
    # config sözlüğü: key = ortam adı, value = config sınıfı.
    # get(config_name, config["default"]) ile bilinmeyen bir ortam adı verilse bile default config seçilir.
    config_class = config.get(config_name, config["default"])

    # Flask uygulamasına config sınıfındaki tüm büyük harfle yazılmış attribute'lar yüklenir.
    # Örnek: config_class.SQLALCHEMY_DATABASE_URI → app.config["SQLALCHEMY_DATABASE_URI"]
    app.config.from_object(config_class)

    # Bu noktadan sonra extension kayıtları ve blueprint kayıtları için fonksiyon çağrıları eklenmesi planlanır:
    # - register_extensions(app)   -> db, migrate, cache, limiter, auth, metrics vb.
    # - register_blueprints(app)   -> auth, catalog, order, payment, admin, recommendation vb.
    # Şimdilik yalnızca health-check endpoint'i tanımlanır.

    @app.get("/health")
    def health():
        """
        Basit health-check endpoint'i.
        Uygulamanın ayakta olduğu ve hangi ortamda çalıştığı hakkında bilgi döndürülür.
        """
        # jsonify ile Python sözlüğü güvenli şekilde JSON HTTP cevabına dönüştürülür.
        # status: Uygulamanın çalıştığını belirtir.
        # env: Kullanılan config ortamını (development/testing/production) gösterir.
        return jsonify({"status": "ok", "env": config_name}), 200

    def register_extensions(app: Flask) -> None:
        """
        Flask extension'larının uygulama örneği ile ilişkilendirildiği fonksiyon.
        Tüm init_app çağrıları merkezi bir yerde toplanır.
        """
        # Veritabanı extension'ı Flask uygulaması ile ilişkilendirilir.
        db.init_app(app)

        # Migration extension'ı Flask uygulaması ve db ile ilişkilendirilir.
        migrate.init_app(app, db=db)

        # Rate limiter extension'ı Flask uygulaması ile ilişkilendirilir.
        # Limit değerleri uygulama config'inden okunabilir hale gelir.
        limiter.init_app(app)

        # JWT extension'ı Flask uygulaması ile ilişkilendirilir.
        # app.config içindeki JWT_... ayarları bu noktadan sonra devreye girer.
        jwt.init_app(app)

        # Cache ve metrics nesneleri için init_app çağrısı bulunmamaktadır.
        # Bu nesneler şu aşamada doğrudan kullanılabilir durumdadır.
        # İlerleyen aşamalarda Redis tabanlı cache entegrasyonu eklendiğinde,
        # burada ek başlatma adımları tanımlanabilir.
    
    # Oluşturulan Flask uygulaması örneği geri döndürülür.
    # Bu örnek hem testlerde hem de gerçek çalışma zamanında kullanılabilir.
    return app

    # İlerleyen aşamalarda aşağıdaki yardımcı fonksiyonların tanımlanması planlanır:    
    # def register_blueprints(app: Flask) -> None:
    #     """auth, catalog, order, payment, admin, recommendation gibi blueprint'ler burada kayıt edilir."""