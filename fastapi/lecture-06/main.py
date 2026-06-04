from fastapi import FastAPI
from routes.product import router
from database import Base, engine
from models.product import Product

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)