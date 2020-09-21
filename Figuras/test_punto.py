import pytest
from Clases import Punto, Circulo

def test_hallar_distancia():
    assert(Punto(-1,0).hallar_distancia(Punto(1,0))) == 2

def test_verificar_dentro_circulo():
    assert(Punto(-1,0).verificar_dentro_circulo(Circulo(4, Punto(1,2)))) == True
