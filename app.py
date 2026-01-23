import sys
import logging
from src.modes import handle_mode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Service starting")

    if len(sys.argv) < 2:
        logger.error("No mode provided. Use: python3 app.py <mode>")
        sys.exit(1)

    mode = sys.argv[1]
    handle_mode(mode)

    logger.info("Service stopping")

if __name__ == "__main__":
    main()