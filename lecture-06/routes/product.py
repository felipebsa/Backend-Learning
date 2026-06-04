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

@router.get("/products/search/{id}")
def get_product_id(id: int, db: Session = Depends(get_db)):
    query = select(Product).where(Product.id==id)
    db_product = db.execute(query).scalars().first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="product id not found")
    return {"message": db_product}

@router.get("/products/search_active/{active}")
def get_products_active(active: bool, db: Session = Depends(get_db)):
    query = select(Product).where(Product.active == active)
    db_products = db.execute(query).scalars().all()
    if not db_products:
        raise HTTPException(status_code=404, detail="no have products in filter")
    return {"message": db_products}

@router.get("/products/search_all")
def get_products_id(db: Session = Depends(get_db)):
    query = select(Product)
    db_products = db.execute(query).scalars().all()
    if not db_products:
        raise HTTPException(status_code=404, detail="no have products")
    return {"message": db_products}

@router.post("/products/register")
def post_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = Product(
        name = product.name,
        category = product.category,
        price = product.price,
        stock = product.stock,
        active = product.active
    )
    db.add(db_product)
    db.commit()
    return {"message": "successful: post_product "}

@router.delete("/products/delete/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    query = select(Product).where(Product.id==id)
    db_product = db.execute(query).scalars().first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="product id not found")
    db.delete(db_product)
    db.commit()
    return {"message": "successful delete_product"}

@router.put("/products/update/{id}")
def put_product(id: int, product: ProductSchema, db: Session = Depends(get_db)):
    query = select(Product).where(Product.id==id)
    db_product = db.execute(query).scalars().first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="product id not found")
    db_product.name = product.name
    db_product.category = product.category
    db_product.price = product.price
    db_product.stock = product.stock
    db_product.active = product.active
    db.commit()
    return {"message": "successful put_product"}