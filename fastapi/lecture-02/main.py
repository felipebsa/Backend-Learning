from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import Base, engine, SessionLocal, Product

app = FastAPI()

Base.metadata.create_all(bind=engine)

class ProductSchema(BaseModel):
    name: str
    value: float
    detail: str
    expired: bool = False

@app.post("/products/")
def create_product(product: ProductSchema):
    db = SessionLocal()
    db_product = Product(
        name=product.name,
        value=product.value,
        detail=product.detail,
        expired=product.expired
    )
    db.add(db_product)
    db.commit()
    db.close()
    return {"message": "product created"}

@app.get("/products/")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products