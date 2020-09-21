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

class Triangulo:
    def __init__(self, punto1, punto2, punto3):
        self.punto1 = punto1
        self.punto2 = punto2
        self.punto3 = punto3
        self.lado1 = punto1.hallar_distancia(punto2)
        self.lado2 = punto1.hallar_distancia(punto3)
        self.lado3 = punto2.hallar_distancia(punto3)

    def hallar_perimetro_triangulo(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro

    def hallar_area_triangulo(self):
        s = self.hallar_perimetro_triangulo()/2
        altura = (2/self.lado1)*math.sqrt(s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3))
        area = (altura*self.lado1)/2
        return area

    def clasificar_triangulo_lados(self):
        if ((self.lado1 == self.lado2) and (self.lado2 == self.lado3) and (self.lado1 == self.lado3)):
            tipo = "Equilatero"
        elif (((self.lado1 == self.lado2) and (self.lado2 == self.lado3) and (self.lado1 != self.lado3)) or ((self.lado1 == self.lado2) and (self.lado2 != self.lado3) and (self.lado1 == self.lado3)) or ((self.lado1 != self.lado2) and (self.lado2 == self.lado3) and (self.lado1 == self.lado3))):
            tipo = "Isosceles"
        elif ((self.lado1 != self.lado2) and (self.lado2 != self.lado3) and (self.lado1 != self.lado3)):
            tipo = "Escaleno"
        return tipo