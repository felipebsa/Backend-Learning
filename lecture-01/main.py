from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "welcome"}

class Product(BaseModel):
    name: str
    value: float
    detail: str
    expired: bool = False

@app.post("/products/")
def create_product(product: Product):
    return {"product": product}

@app.get("/products/{product_id}")
def product(product_id):
    if product_id > 50:
        raise HTTPException(status_code=404, detail="product not found")
    return {"product": product_id}