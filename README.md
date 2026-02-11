# cloud-data-platform

A small FastAPI service built as a learning project, with production-style basics:
- health endpoint
- runtime modes
- request timing + structured logs
- request IDs (logged and returned to clients)
- tests

## Requirements
- Python 3.x
- macOS/Linux (works on Windows too, but commands may differ)

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate