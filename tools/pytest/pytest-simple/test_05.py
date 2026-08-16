from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()

class SchemaSum(BaseModel):
    a: int
    b: int

@app.post("/sum", status_code=201)
def sum_n(numbers: SchemaSum):
    result = numbers.a + numbers.b
    return {"mensagem": result}

client = TestClient(app)

def test_sum_n():
    response = client.post("/sum", json={"a": 1, "b": 3})
    assert response.status_code == 201
    assert response.json() == {"mensagem": 4}