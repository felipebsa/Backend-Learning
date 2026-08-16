import pytest

@pytest.fixture(scope="module")
def numeros():
    print("Criando lista...")
    return [1, 2, 3, 4, 5]

def test_tamanho(numeros):
    assert len(numeros) == 5

def test_soma_total(numeros):
    assert sum(numeros) == 15