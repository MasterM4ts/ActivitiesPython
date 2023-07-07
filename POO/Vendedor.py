class Vendedor():


    def __init__(self,nome,vendas):
        self.nome = nome
        self.vendas = vendas
    

    def vendeu(self,vendas):
        self.vendas = vendas
        print(self.vendas)
    
    
    def bateu_meta(self,meta):
        self.meta = meta
        if self.vendas > meta:
            print("Bateu Meta")
        else:
            print("Não Bateu a Meta")
            