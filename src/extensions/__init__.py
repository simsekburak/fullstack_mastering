"""
Flask extension'larının merkezi tanım ve init noktası.

Bu modül, uygulama boyunca kullanılacak ortak extension örneklerini barındırır.
Extension nesneleri burada global olarak tanımlanır ve create_app içinde init edilir.
"""

from .db import db
from .migrate import migrate
from .cache import cache
from .limiter import limiter
from .auth import jwt
from .metrics import metrics

# Bu import'lar sayesinde:
# - extensions.db.db
# - extensions.migrate.migrate
# - extensions.cache.cache
# - extensions.limiter.limiter
# - extensions.auth.jwt
# - extensions.metrics.metrics
# gibi tek bir merkezden erişim sağlanır.