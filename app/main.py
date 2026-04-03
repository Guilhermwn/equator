from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers import items
from app.ui.pages import home_page

app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/", response_class=HTMLResponse)
def index():
    return home_page()