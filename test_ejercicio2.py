import pytest
from Ejercicio2 import numero_par

def test_par():
    assert numero_par(50) == True  

@pytest.mark.parametrize(
    "input_a, expected",
    [
        (10, True),
        (7, False),
        (-765, False),
        (-896, True)
    ]
)
def test_par_multi(input_a, expected):
    assert numero_par(input_a) == expected