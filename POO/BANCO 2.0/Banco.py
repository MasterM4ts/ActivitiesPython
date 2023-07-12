from time import sleep
class Banco():
    
    
    def __init__(self,nome,cpf,senha):
        self.nome = nome      
        self.__saldo = 0
        self.__cpf = cpf
        self.__senha = senha

    
    def extrato(self,senha):
        if senha == self.__senha:
            return self.__saldo
        
        
        else:
            print("I| Senha Invalida I|")
        

    def sacar(self,senha):
        if senha == self.__senha:
            valor = float(input("I| Digite o Valor a Sacar:\n>> "))
            if valor > 5000:
                print("I| Aguarde 10 Segundos o Saque está sendo Processado.")
                sleep(10)
            self.__saldo -= valor
            print("I| Saque Feito com Sucesso I|")
            return self.__saldo
        

        else:
            print("I| Senha Invalida I|")


    def depositar(self,valor):
        if valor > 5000:
            print("I| Aguarde 10 Segundos o Deposito está sendo Processado.")
            sleep(10)
        self.__saldo += valor 
        print("I| Deposito Feito com Sucesso I|")