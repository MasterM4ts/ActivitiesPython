from Cadastro import*
from Cartao import*
class Compra(Cadastro):

    def __init__(self):
        pass
        
    
    def comprar(self,produto,valor):
        while True:
            try:
                print("-"*16)
                forma = int(input("I| (1) >> Debito\n(2) >> Crédito\n>> "))
            

            except ValueError:
                print("-"*30)
                print("I| Digite Somente as Opções I|")
                print("-"*30)
            

            else:
                print(f"I| Produto...{produto}")
                print(f"I| Valor do Produto...{valor}")
                os.system("pause")
                os.system("cls")
                Cartao.forma_pagamento(forma)
                break