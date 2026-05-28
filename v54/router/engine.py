from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/event")
async def event(req: Request):
    data = await req.json()
    
    return {
        "event": data,
        "route": "dynamic-industry-selector",
        "status": "processed"
    }
