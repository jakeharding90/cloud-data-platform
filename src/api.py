from fastapi import FastAPI, HTTPException
from src.modes import handle_mode, InvalidModeError

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/run/{mode}")
def run_mode(mode: str):
    try:
        handle_mode(mode)
        return {"message": f"Mode '{mode}' executed"}
    except InvalidModeError as e:
        raise HTTPException(status_code=400, detail=str(e))