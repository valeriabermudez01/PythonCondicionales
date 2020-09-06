import pytest
from Ejercicio1 import edad

def test_edad():
    assert edad(11,2010) == 71 

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (21,2020,71),
        (3,2003,70),
        (edad(10,2010),2070,70)
    ]
)
def test_edad_multi(input_a, input_b, expected):
    assert edad(input_a, input_b) == expected
