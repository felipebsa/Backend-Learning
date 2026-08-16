from database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.client import router as client_router
from models.client import Client

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(client_router)