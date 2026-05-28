from prometheus_client import Counter

runtime_requests = Counter(
    "runtime_requests",
    "Runtime Requests"
)
