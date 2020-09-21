import pytest
from Clases import Circulo, Punto

def test_hallar_area_circulo():
    assert(Circulo(3, Punto(0,0)).hallar_area_circulo()) == pytest.approx(28.27, 0.01)

@pytest.mark.parametrize(
    "input_circulo, expected",
    [
        (Circulo(5,(2,0)), 78.53),
        (Circulo(2,(0,2)), 12.56)
    ]
)
def test_hallar_area_circulo_multi(input_circulo, expected):
    assert(input_circulo.hallar_area_circulo()) == pytest.approx(expected, 0.01)

def test_hallar_perimetro_circulo():
    assert(Circulo(3, Punto(0,0)).hallar_perimetro_circulo()) == pytest.approx(18.84, 0.01)

@pytest.mark.parametrize(
    "input_circulo, expected",
    [
        (Circulo(5,(2,0)), 31.41),
        (Circulo(2,(0,2)), 12.56)
    ]
)
def test_hallar_perimetro_circulo_multi(input_circulo, expected):
    assert(input_circulo.hallar_perimetro_circulo()) == pytest.approx(expected, 0.01)