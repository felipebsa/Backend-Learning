from pydantic import BaseModel
from datetime import datetime

class SchemaClient(BaseModel):
    name: str
    cpf: str
    date: datetime
    active: bool

class SchemaClientResponse(BaseModel):
    id: int
    name: str
    cpf: str
    date: datetime
    active: bool

    model_config = {"from_attributes": True}