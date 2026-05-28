from fastapi import FastAPI

app = FastAPI()

@app.get("/realestate/listings")
def listings():
    return {"service":"property-intelligence","monetization":"lead_generation"}
