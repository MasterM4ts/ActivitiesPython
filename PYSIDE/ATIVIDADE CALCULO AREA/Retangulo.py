from Shape import Shape
from PySide6.QtWidgets import QLabel


class Retangulo(Shape):
    def __init__(self, base, altura, cor):
        super().__init__(cor)
        self.base = base
        self.altura = altura
    
    
    def calcular_area(self):
        return self.base * self.altura
        
    