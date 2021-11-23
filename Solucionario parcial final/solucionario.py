from math import pi

class Figura:
    def __init__(self, nombre, color, ancho, alto):
        self.nombre = nombre
        self.color = color
        self.ancho = ancho
        self.alto = alto
    
    def calculo_area(self):
        calculo = self.ancho * self.alto
        print("El área de la figura " + self.nombre + " es: " + str(calculo))


class Cuadrado(Figura):
    def __init__(self, nombre, color, lado1, lado2):
        super().__init__(nombre, color, lado1, lado2)
    
    def calculo_area(self):
        return super().calculo_area()

class Rectangulo(Figura):

    def __init__(self, nombre, color, base, altura):
        super().__init__(nombre, color, base, altura)
    
    def calculo_area(self):
        return super().calculo_area()

cuadrado = Cuadrado("Cuadrado", "rosado", 5, 5)
cuadrado.calculo_area()


rectangulo = Rectangulo("Rectangulo", "verde", 10, 5)
rectangulo.calculo_area()

#aunque el circulo es distinto, se hereda el método calculo_area, el cual se sobre escribe para este caso.
#Si no se hereda de Figura es valido, ya que los atributos son diferente

class Circulo(Figura):
    
    def __init__(self, diametro):
        self.diametro = diametro

    def calculo_area(self):
        r = self.diametro / 2
        area = pi * (r **2)
        print("El área del circulo es: " + str(area))

circulo = Circulo(38)
circulo.calculo_area()
