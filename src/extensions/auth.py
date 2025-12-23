"""
JWT tabanlı kimlik doğrulama için Flask-JWT-Extended extension tanımı.
Erişim ve yenileme token'larının yönetimi için kullanılır.
"""

from flask_jwt_extended import JWTManager

# Uygulama genelinde kullanılacak JWTManager örneği.
# init_app ile Flask uygulamasına bağlama işlemi daha sonra yapılır.
jwt = JWTManager()