import pytest
from Clases import Rectangulo, Punto

@pytest.mark.parametrize(
    "rectangulo, expected",
    [
        (Rectangulo(Punto(1,0), Punto(1,1), Punto(4,0), Punto(4,1)), 3),
        (Rectangulo(Punto(0,0), Punto(0,-2), Punto(5,0), Punto(5,-2)), 10)
    ]
)
def test_hallar_area_rectangulo_multi(rectangulo, expected):
    assert(rectangulo.hallar_area_rectangulo()) == pytest.approx(expected, 0.01)

@pytest.mark.parametrize(
    "rectangulo, expected",
    [
        (Rectangulo(Punto(1,0), Punto(1,1), Punto(4,0), Punto(4,1)), 8),
        (Rectangulo(Punto(0,0), Punto(0,-2), Punto(5,0), Punto(5,-2)), 14)
    ]
)
def test_hallar_perimetro_rectangulo_multi(rectangulo, expected):
    assert(rectangulo.hallar_perimetro_rectangulo()) == pytest.approx(expected, 0.01)