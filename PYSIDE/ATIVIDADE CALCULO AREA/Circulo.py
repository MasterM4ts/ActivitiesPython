from Shape import Shape
from PySide6.QtWidgets import QLabel

class Circulo(Shape):
    def __init__(self, raio, cor):
        super().__init__(cor)
        self.raio = raio
        
        
    def calcular_area(self):
        return 3.14 * (self.raio ** 2)
        