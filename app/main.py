from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routers import math

BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI()
app.include_router(math.router, prefix="/math", tags=["math"])
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")
