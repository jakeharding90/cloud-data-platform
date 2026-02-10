import time
import logging
import fastapi
import uuid
import os
from fastapi import Request
from fastapi import FastAPI, HTTPException
from src.modes import handle_mode, InvalidModeError, get_valid_modes

app = FastAPI()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger("api")

APP_ENV = os.getenv("APP_ENV", "dev").lower()
PORT = int(os.getenv("PORT", "8000"))

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
    response.headers["X-Request-ID"] = request_id
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
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api:app", host="0.0.0.0", port=PORT, reload=(APP_ENV == "dev"))