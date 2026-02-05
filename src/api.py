import time
import logging
import fastapi
import uuid
from fastapi import Request
from fastapi import FastAPI, HTTPException
from src.modes import handle_mode, InvalidModeError, get_valid_modes

app = FastAPI()

logger = logging.getLogger("api")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id

    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    logger.info(
        "request_id=%s %s %s completed in %.4fs",
        request_id,
        request.method,
        request.url.path,
        duration,
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