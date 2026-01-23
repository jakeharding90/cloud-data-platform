import sys
import logging

logger = logging.getLogger(__name__)

def handle_mode(mode):
    if mode == "dev":
        logger.info("development mode enabled")
    elif mode == "prod":
        logger.info("production mode enabled")
    else:
        logger.error(f"Unknown mode: {mode}")
        sys.exit(1)