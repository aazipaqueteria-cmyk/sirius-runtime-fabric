from prometheus_client import Counter

runtime_requests = Counter(
    "runtime_requests_total",
    "Total runtime requests"
)

def track():
    runtime_requests.inc()
