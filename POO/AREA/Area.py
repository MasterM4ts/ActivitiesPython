#Abstração#
class Area():

    
    def __init__(self,tamanho_lado):
        self.tamanho_lado = tamanho_lado


    def mostrar_area(self,lado):
        self.area = lado*lado
        return self.area
        

    
    def mudar_valor_lado(self,lado):
        self.area = lado*lado
        return self.area  