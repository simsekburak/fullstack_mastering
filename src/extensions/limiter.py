"""
Rate limiting (istek sayısı sınırlama) için Flask-Limiter extension tanımı.
API'nin aşırı isteklerden korunması için kullanılır.
"""

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Limiter nesnesi, her istek için istemci IP adresini temel alan bir key fonksiyonu ile tanımlanır.
# init_app çağrısı ile Flask uygulaması ile entegrasyon daha sonra sağlanır.
limiter = Limiter(
    key_func=get_remote_address,
    # Varsayılan limitler config üzerinden ayarlanabilir.
    default_limits=[],
)