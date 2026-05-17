from fastapi import FastAPI
from database import engine, Base
from routes.book import router
from models.book import Book

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)

