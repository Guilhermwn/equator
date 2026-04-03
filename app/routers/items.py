from fastapi import APIRouter, HTTPException
from app.models.item import Item

router = APIRouter()

# Mock database
items_db: dict[int, dict] = {
    1: {"id": 1, "name": "exemplo"}
}

@router.get("/")
def list_items():
    return list(items_db.values())

@router.post("/")
def create_item(item: Item):
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Item com esse ID já existe")
    
    items_db[item.id] = item.model_dump()
    return items_db[item.id]