from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/ola")
def ola():
    return {"mensagem": "oi"}

client = TestClient(app)

def test_rota_ola():
    response = client.get("/ola")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "oi"}