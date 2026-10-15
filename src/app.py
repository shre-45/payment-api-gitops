
from fastapi import FastAPI

app = FastAPI(title="Payment API")


@app.get("/")
def home():
    return {
        "application": "payment-api",
        "version": "1.1",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
