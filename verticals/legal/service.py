from fastapi import FastAPI

app = FastAPI()

@app.get("/legal/consultas")
def consultas():
    return {"service":"legal-asa-service","billing":"per_hour","mode":"PaaS-Legal"}

@app.get("/legal/expediente")
def expediente(q: str):
    return {"query": q, "source":"judicial_scraper_ready"}
