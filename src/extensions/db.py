"""
Veritabanı işlemleri için SQLAlchemy extension tanımı.
Bu dosyada yalnızca db nesnesi tanımlanır; init işlemleri create_app içinde yapılır.
"""

from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy için global extension nesnesi oluşturulur.
# Uygulama örneği (app) ile bağlama işlemi daha sonra init_app üzerinden yapılır.
db = SQLAlchemy()