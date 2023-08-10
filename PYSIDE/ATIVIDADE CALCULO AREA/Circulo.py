import Shape

class Circulo(Shape):
    def __init__(self, cor, raio):
        super().__init__(self, cor)
        self.raio = raio
    
    
    def calculo_area(self):
        return 3.14 * (self.raio**2)