import Shape 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QLineEdit, QHBoxLayout, QVBoxLayout

class Retangulo(Shape):
    def __init__(self, cor, base, altura):
        super().__init__(self, cor)
        self.altura = altura
        self.base = base
        
        


    
    def caculo_area(self):
        area = self.base * self.altura
        print("A área do Retângulo é: {area}")    