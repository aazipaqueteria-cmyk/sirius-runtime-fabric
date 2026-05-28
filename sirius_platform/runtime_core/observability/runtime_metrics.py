from prometheus_client import Counter

runtime_requests = Counter(
    "runtime_requests_total",
    "Runtime Total Requests"
)
