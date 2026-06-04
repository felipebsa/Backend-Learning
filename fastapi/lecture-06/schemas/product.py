from pydantic import BaseModel

class ProductSchema(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int
    active: bool