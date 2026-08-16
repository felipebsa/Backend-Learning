from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.client import Client
from schemas.client import SchemaClient, SchemaClientResponse
from database import get_db


router = APIRouter()

@router.post("/client/register", response_model=SchemaClientResponse)
def create_client(client: SchemaClient, db: Session = Depends(get_db)):
    db_client = Client(
        name = client.name,
        cpf = client.cpf,
        date = client.date,
        active = client.active
    )
    db.add(db_client)
    db.commit()
    return db_client