"""
Veritabanı şema değişikliklerinin yönetimi için Flask-Migrate extension tanımı.
Alembic tabanlı migration işlemleri için kullanılır.
"""

from flask_migrate import Migrate

# Migration işlemleri için global Migrate nesnesi oluşturulur.
# Uygulama ve db bağlantısı init_app çağrısı ile daha sonra sağlanır.
migrate = Migrate()