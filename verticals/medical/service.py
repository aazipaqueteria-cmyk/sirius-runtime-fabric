from fastapi import FastAPI

app = FastAPI()

@app.get("/medical/appointments")
def appointments():
    return {"billing":"per_session","service":"medical-saas"}

@app.get("/medical/patients")
def patients():
    return {"database":"encrypted_patient_index"}
