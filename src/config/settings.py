import os
from typing import Optional

class Config:
    """Temel config sınıfı - tüm ortamlar için ortak ayarlar"""
    
    # Flask temel ayarları
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    # SECRET_KEY: Session, CSRF token gibi güvenlik özellikleri için kullanılır
    # Production'da mutlaka güçlü, rastgele bir değer olmalı
    
    # Database ayarları
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost:5432/marketplace_db"
    )
    # PostgreSQL bağlantı string'i
    # Format: postgresql://kullanici:sifre@host:port/veritabani_adi
    
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    # SQLAlchemy'nin model değişikliklerini takip etmesini kapatır (performans için)
    
    SQLALCHEMY_ECHO: bool = False
    # SQL sorgularını console'a yazdırır (debug için, production'da False)
    
    # Redis ayarları (cache ve rate limiting için)
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    # Redis bağlantı URL'i
    
    # JWT ayarları
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", SECRET_KEY)
    # JWT token'ları imzalamak için kullanılan secret key
    JWT_ACCESS_TOKEN_EXPIRES: int = 3600  # 1 saat (saniye cinsinden)
    JWT_REFRESH_TOKEN_EXPIRES: int = 86400 * 7  # 7 gün
    
    # Rate limiting ayarları
    RATELIMIT_ENABLED: bool = True
    RATELIMIT_STORAGE_URL: str = REDIS_URL
    # Rate limiting için Redis kullanılacak
    
    # CORS ayarları
    CORS_ORIGINS: list = ["*"]  # Development için, production'da spesifik domain'ler belirtilmeli
    
    # Logging ayarları
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    # Log seviyesi: DEBUG, INFO, WARNING, ERROR, CRITICAL


class DevelopmentConfig(Config):
    """Development ortamı için özel ayarlar"""
    DEBUG: bool = True
    SQLALCHEMY_ECHO: bool = True  # Development'ta SQL sorgularını görmek için
    LOG_LEVEL: str = "DEBUG"


class TestingConfig(Config):
    """Test ortamı için özel ayarlar"""
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "postgresql://user:password@localhost:5432/test_marketplace_db"
    # Test için ayrı bir veritabanı kullanılmalı
    WTF_CSRF_ENABLED: bool = False  # Test'te CSRF kontrolü kapalı


class ProductionConfig(Config):
    """Production ortamı için özel ayarlar"""
    DEBUG: bool = False
    SQLALCHEMY_ECHO: bool = False
    LOG_LEVEL: str = "WARNING"
    # Production'da daha az log, sadece önemli olaylar


# Config mapping - ortam değişkenine göre hangi config'in kullanılacağını belirler
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}