from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from starlette.staticfiles import StaticFiles

app = FastAPI()

PROJECT_ROOT = Path(__file__).parent.parent

# This should come AFTER all other endpoints
app.mount("/", StaticFiles(directory=PROJECT_ROOT / "static", html=True))