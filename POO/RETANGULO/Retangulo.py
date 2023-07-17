#Abstração#
class Retangulo():

    
    def __init__(self,base,altura,):
        self.base = base
        self.altura = altura


    def mostrar_info_retangulo(self,base,altura):
        self.area = base * altura
        self.perimetro = 2 * (base + altura)
        self.rodape = self.area * 15/100
        print(f"I| Área: {self.area}")
        print(f"I| Perimetro: {self.perimetro}")
        print(f"I| Rodapé: {self.rodape}")
    

    def mostrar_area(self,base,altura):
        self.area = base * altura
        return self.area
    

    def mostrar_perimetro(self,base,altura):
        self.perimetro = 2 * (base + altura)
        return self.perimetro
    

    def mostrar_rodape(self,area):
        self.rodape = area * 15/100
        return self.rodape