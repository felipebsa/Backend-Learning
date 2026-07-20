

def test_create_client(client_db):
    response = client_db.post("/client/register", json={
        "name": "s",
        "cpf": "123",
        "date": "2026-01-01T00:00:00",
        "active": True
    })
    assert response.status_code == 200
    assert response.json()["cpf"] == "123"