#Abstração#
class Bola():


    def __init__(self,cor,circunferencia,material,marca):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        self.marca = marca

    
    def troca_Cor(self,cor):
        self.cor = cor
        print("I| Cor Alterada")
    

    def mostra_Bola(self):
        print(f"I| Cor da Bola: {self.cor}")
        print(f"I| Material da Bola: {self.material}")
        print(f"I| Circunferência da Bola: {self.circunferencia}")
        print(f"I| Marca da Bola: {self.marca}")    