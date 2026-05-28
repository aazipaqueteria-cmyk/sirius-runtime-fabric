from fastapi import FastAPI
from sirius_platform.runtime_core.observability.runtime_metrics import runtime_requests

app = FastAPI(
    title="Sirius Runtime",
    version="1.1"
)

@app.get("/health")
async def health():

    runtime_requests.inc()

    return {
        "status":"healthy"
    }

@app.get("/business/runtime")
async def runtime():

    runtime_requests.inc()

    return {
        "runtime":"active",
        "fabric":"distributed"
    }
