from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, Base, session_base

app = FastAPI()
Base.metadata.create_all(engine)