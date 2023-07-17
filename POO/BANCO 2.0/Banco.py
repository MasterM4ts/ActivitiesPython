#Encapsulamento#
from time import sleep
class Banco():
    
    
    def __init__(self,nome,cpf,senha):
        self.nome = nome      
        self.__saldo = 0
        self.__cpf = cpf
        self.__senha = senha

    
    def extrato(self,senha):
        if senha == self.__senha:
            print(f"I| Nome:  | {self.nome}")
            print(f"I| CPF:   | {self.__cpf}")
            print(f"I| Saldo: | R${self.__saldo}")
        
        
        else:
            print("-"*20)
            print("I| Senha Invalida I|")
            print("-"*20)
        

    def sacar(self,senha):
        if senha == self.__senha:
            
            
            while True:
                try:
                    valor = float(input("I| Digite o Valor a Sacar:\n>> "))
                
                
                except ValueError:
                    print("-"*27)
                    print("I| Digite Ápenas Números I|")
                    print("-"*27)
                
                
                else:
                    if valor >= 5000:
                        print("-"*10)
                        print("I| Aguarde 10 Segundos o Saque está sendo Processado.")
                        sleep(10)


                    self.__saldo -= valor
                    print("-"*29)
                    print("I| Saque Feito com Sucesso I|")
                    print("-"*29)
                    return self.__saldo
        

        else:
            print("I| Senha Invalida I|")


    def depositar(self,valor):
        if valor >= 5000:
            print("I| Aguarde 10 Segundos o Deposito está sendo Processado.")
            sleep(10)

        
        self.__saldo += valor 
        print("-"*32)
        print("I| Deposito Feito com Sucesso I|")
        print("-"*32)

    
    def esc_senha(self,cpf):
        if cpf == self.__cpf:
            print("-"*19)
            print("I| Alterar Senha I|")
            senha = input("I| Digite sua Nova Senha:\n>> ")
            self.__senha = senha
        

        else:
            print("-"*18)
            print("I| CPF Invalido I|")
            print("-"*18)