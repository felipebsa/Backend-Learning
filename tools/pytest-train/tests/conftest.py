import pytest
from fastapi.testclient import TestClient
from main import app
from database import get_db, SessionLocal, engine, Base
from models.client import Client

@pytest.fixture
def client_db():
    # 1. Cria as tabelas (garante que existem)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    db.query(Client).delete()
    db.commit()
    # 2. Sobrescreve a dependency get_db pra usar essa mesma sessão
    def override_get_db():
        yield db
    app.dependency_overrides[get_db] = override_get_db

    test_client = TestClient(app)

    yield test_client  # <- aqui é onde o teste "roda"

    # 3. Depois do teste: limpa os dados e fecha a sessão
    db.rollback()
    db.query(Client).delete()
    db.commit()
    db.close()