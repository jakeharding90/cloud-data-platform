import time
import fastapi
from fastapi import Request
from fastapi import FastAPI, HTTPException
from src.modes import handle_mode, InvalidModeError, get_valid_modes

app = FastAPI()

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    print(
        f"{request.method} {request.url.path} "
        f"completed in {duration:.4f}s"
    )

    return response

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/modes")
def list_modes():
    return {"valid_modes": get_valid_modes()}

@app.get("/run/{mode}")
def run_mode(mode: str):
    try:
        handle_mode(mode)
        return {"message": f"Mode '{mode}' executed"}
    except InvalidModeError as e:
        raise HTTPException(status_code=400, detail=str(e))