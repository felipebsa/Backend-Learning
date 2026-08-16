import pytest

def f_sum(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_f_sum(a, b, expected):
    assert f_sum(a, b) == expected