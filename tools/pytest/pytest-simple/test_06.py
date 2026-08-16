from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from pydantic import BaseModel

engine = create_engine("sqlite:///:memory:")
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()

# sessoes reais

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# sessoes para teste 

engine_test = create_engine("sqlite:///:memory:")
SessionTest = sessionmaker(bind=engine_test)

def get_db_test():
    db = SessionTest()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client_test():
    app.dependency_overrides[get_db] = get_db_test
    yield TestClient(app)
    app.dependency_overrides.clear()

# schema

class SchemaItensCreate(BaseModel):
    name: str

# rota real

@app.post("/itens", status_code=201)
def create_item(item: SchemaItensCreate):
    name = item.name
    return {"mensagem": name}

# teste da rota

def test_criar_item(client_test):
    response = client_test.post("/itens", json={"name": "caneta"})
    assert response.status_code == 201