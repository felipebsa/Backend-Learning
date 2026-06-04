from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.product import Product
from schemas.product import ProductSchema
from database import get_db

router = APIRouter()

@router.get("/")
def get_home():
    return {"message": "get_home successful"}

@router.get("/products/{id}")
def get_product_id(id: int, db: Session = Depends(get_db)):
    query = select(Product).where(Product.id == id)
    db_product = db.execute(query).scalars().first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="product not found")
    return {"message": db_product}