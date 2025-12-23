"""
Önbellekleme (caching) mekanizması için extension tanımı.
Gelişmiş kullanımda Flask-Caching veya benzeri bir araç ile entegre edilebilir.
"""

from typing import Any


class SimpleCache:
    """
    Minimal bir cache iskeleti.
    Gerçek cache implementasyonu ilerleyen aşamalarda Redis tabanlı hale getirilebilir.
    """

    def __init__(self) -> None:
        # Bellek içi basit bir sözlük kullanılır (sadece geliştirme/test iskeleti için).
        self._store: dict[str, Any] = {}

    def get(self, key: str) -> Any:
        """
        Verilen anahtar için cache'ten değer döndürülür.
        Anahtar bulunamazsa None döner.
        """
        return self._store.get(key)

    def set(self, key: str, value: Any) -> None:
        """
        Verilen anahtar için cache'te değer saklanır.
        Süre (TTL) yönetimi bu basit iskelette bulunmaz.
        """
        self._store[key] = value


# Uygulama boyunca kullanılacak global cache örneği oluşturulur.
# Gerçek bir Redis tabanlı cache ile değiştirilmeye uygun olacak şekilde basit tutulur.
cache = SimpleCache()