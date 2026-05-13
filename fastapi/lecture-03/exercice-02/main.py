from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, Base, session_base

app = FastAPI()
base.metadata.create_all(engine)