import pytest
from Clases import Triangulo, Punto

@pytest.mark.parametrize(
    "triangulo, expected",
    [
        (Triangulo(Punto(0,0),Punto(3,0),Punto(0,4)), 12),
        (Triangulo(Punto(0,0),Punto(0,5),Punto(5,0)), 17.07)
    ]
)

def test_hallar_perimetro_triangulo_multi(triangulo, expected):
    assert triangulo.hallar_perimetro_triangulo() == pytest.approx(expected, 0.1)

@pytest.mark.parametrize(
    "triangulo, expected",
    [
        (Triangulo(Punto(0,0),Punto(1,0),Punto(0.5,1)), 0.5),
        (Triangulo(Punto(0,0),Punto(0,-4),Punto(-2,0)), 4)
    ]
)
def test_hallar_area_triangulo_multi(triangulo, expected):
    assert triangulo.hallar_area_triangulo() == pytest.approx(expected, 0.1)

def test_clasificar_triangulo_lados():
    assert(Triangulo(Punto(0,0), Punto(3,0), Punto(0,4)).clasificar_triangulo_lados()) == 'Escaleno'
