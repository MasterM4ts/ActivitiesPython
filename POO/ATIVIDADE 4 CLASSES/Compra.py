from Cadastro import*
from Cartao import*
class Compra(Cadastro):

    def __init__(self, nome, cpf, telefone, email, endereco, senha):
        super().__init__(nome, cpf, telefone, email, endereco, senha)
        self.carrinho_compra = 0
        

    
    def carrrinho(self,produto,valor):
        self.carrinho_compra += 1
        print(f"I| Produto...{produto}")
        print(f"I| Valor do Produto...{valor}")
        print("I| Carrinho Adicionou Produto I|")
        os.system("pause")
        os.system("cls")
    
    
    def comprar(self):
        self.carrinho_compra = 0
        forma = int(input("I| (1) >> Debito\n(2) >> Crédito\n>> "))
        Cartao.forma_pagamento(forma)