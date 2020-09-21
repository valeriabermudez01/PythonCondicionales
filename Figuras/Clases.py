import math



class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hallar_distancia(self, punto):
        distancia = math.sqrt(math.pow(self.x - punto.x,2) + math.pow(self.y - punto.y,2))
        return distancia

    def verificar_dentro_circulo(self, circulo):
        if self.hallar_distancia(circulo.centro) <= circulo.radio:
            return True
        else:
            return False

class Circulo:
    def __init__(self, radio, centro):
        self.radio = radio
        self.centro = centro

    def hallar_area_circulo(self):
        area = math.pi * math.pow(self.radio, 2)
        return area

    def hallar_perimetro_circulo(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro 

