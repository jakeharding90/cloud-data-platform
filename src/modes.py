import logging

logger = logging.getLogger(__name__)

class InvalidModeError(ValueError):
    pass

def handle_mode(mode: str) -> None:
    if mode == "dev":
        logger.info("development mode enabled")
    elif mode == "prod":
        logger.info("production mode enabled")
    else:
        logger.error(f"Unknown mode: {mode}")
        raise InvalidModeError(f"Unknown mode: {mode}")