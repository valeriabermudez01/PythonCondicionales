import pytest
from condicionales import palabras

def test_palabras():
    assert palabras("Hola") == ("H", "a")

@pytest.mark.parametrize(
    "input_a, expected",
    [
        ("Hola", ("H","a")),
        ("Prueba", ("P","a")),
        ("v", ("v", "v")),
        ("5465", ("5", "5"))
    ]
)
def test_palabras_multi(input_a, expected):
    assert palabras(input_a) == expected
