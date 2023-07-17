from Cadastro import*
from Banco import*
class Cartao(Cadastro):


    def __init__(self, nome, cpf, telefone, email, endereco, senha, cartao):
        super().__init__(nome, cpf, telefone, email, endereco, senha)
        self.__cartao = cartao
        self.__saldo_cartao = 0
        self.__senha = senha
        

    def cadastro(self):
        Cadastro.cadastro()
        cartao = input("I| Digite o Número do Cartão:\n>> ")
        return cartao
         

    def depositar(self,valor):
        self.__saldo_cartao += valor
        print("I| Deposito Concluido I|")


    def sacar(self,senha):
        if senha == self.__senha:
            valor = float(input("I| Digite o Valor a ser Sacado:\n>> "))
            self.__saldo_cartao -= valor
            return self.__saldo_cartao
        else:
            print("I| Senha Invalida I|")
            os.system("pause")
            os.system("cls")


    def parcelamento(self):
        valor = float(input("I| Digite o Valor da Compra:\n>> "))
        qtd_parcela = int(input("I| Digite em Quantas Vezes Deseja Parcelar:\n>>"))
        valor = valor / qtd_parcela
        print(f"I| Valor por Parcela...{valor}")
        print("I| Compra Realizada com Sucesso I|") 
        os.system("pause")
        os.system("cls")
        
    
    def forma_pagamento(self,forma):
        if forma == 1:
            senha = pwinput("I| Digite a sua Senha do Cartão:\n>> ")
            
            
            if senha == self.__senha:
                print("I| Debito I|")
                valor = float(input("I| Digite o valor da Compra:\n>> "))
                
                
                if valor > self.__saldo_cartao:
                    print("I| Saldo do Cartão Insuficiente.")
                    os.system("pause")
                    os.system("cls")
                

                else:
                    self.__saldo_cartao -= valor
                    print("I| Compra Realizada com Sucesso I|")
            
            
            else:
                print("I| Senha Invalida I|")
                os.system("pause")
                os.system("cls")
        
        
        if forma == 2:
            print("I| Credito I|")
            Cartao.parcelamento()