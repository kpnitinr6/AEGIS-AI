from fastapi import FastAPI

app = FastAPI(
    title="AEGIS AI",
    version="0.0.1",
    description="Institutional AI Trading Platform"
)

@app.get("/")
def root():
    return {
        "application": "AEGIS AI",
        "version": "0.0.1",
        "status": "running"
    }