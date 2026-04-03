from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     prince: float
#     available: bool = True

class Item(BaseModel):
    id: int
    name: str