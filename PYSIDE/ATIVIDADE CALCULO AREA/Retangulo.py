import Shape 

class Retangulo(Shape):
    def __init__(self, cor, base, altura):
        super().__init__(self, cor)
        self.altura = altura
        self.base = base
        
    
    def caculo_area(self):
        area = self.base * self.altura
        print("A área do Retângulo é: {area}")    