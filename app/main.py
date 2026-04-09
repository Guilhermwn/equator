from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from app.routers import math

BASE_DIR = Path(__file__).parent

app = FastAPI()

env = Environment(
    loader=FileSystemLoader(BASE_DIR / "templates"),
    variable_start_string="[[",  # substitui {{
    variable_end_string="]]",  # substitui }}
)
templates = Jinja2Templates(env=env)

app.include_router(math.router, prefix="/math", tags=["math"])


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
