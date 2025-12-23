"""
Uygulama metrikleri için Prometheus tabanlı izleme iskeleti.
Temel metrikler (istek sayısı, hata sayısı vb.) ilerleyen aşamalarda burada tanımlanır.
"""

from prometheus_client import Counter, Histogram

# Toplam istek sayısını ölçmek için counter örneği.
http_requests_total = Counter(
    "http_requests_total",
    "Toplam HTTP istek sayısı",
    ["method", "endpoint", "http_status"],
)

# İstek süresini ölçmek için histogram örneği.
http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "HTTP istek süreleri (saniye cinsinden)",
    ["method", "endpoint"],
)


class Metrics:
    """
    Metrik nesnelerini sarmalayan yardımcı sınıf.
    İlerleyen aşamalarda ek metrikler bu sınıfa eklenebilir.
    """

    def __init__(self) -> None:
        self.requests_total = http_requests_total
        self.request_duration = http_request_duration_seconds


# Uygulama genelinde kullanılacak metrics sarmalayıcı nesnesi.
metrics = Metrics()