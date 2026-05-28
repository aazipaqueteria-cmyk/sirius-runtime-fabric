from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/runtime")
def runtime():
    return {"mesh":"active"}
