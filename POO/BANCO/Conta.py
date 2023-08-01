#Abstração#
from time import sleep
class Conta():
    
    
    def __init__(self,nome,conta,agencia,cpf,fone):
        self.nome = nome
        self.conta = conta
        self.agencia = agencia
        self.saldo = 0
        self.cpf = cpf
        self.fone = fone


    def saque(self,saldo):
        if saldo < 0:
            print("I| Saque Invalido I|\nI| Quantia de Saque Negativa I|")
        

        elif saldo > self.saldo:
            print("I| Saque Invalido I|\nI| Quantia de Saque Acima do Saldo da Conta I|")


        else:
            self.saldo -= saldo
            print(f"I| R${self.saldo}")
    

    def deposito(self,saldo):
        if saldo >= 5000:
            print("I| \"Aguarde 10 Segundos\"\nI| Estamos Revisando Seu Deposito I|")
            delay = 10
            sleep(delay)
            print("I| \"Deposito Confirmado\" I|")
            self.saldo += saldo
            print(f"I| R${self.saldo}")
        

        else:
            print("I| \"Deposito Confirmado\" I|")
            self.saldo += saldo
            print(f"I| R${self.saldo}")           

    
    def extrato(self):
        print(f"I| Nome: {self.nome}")
        print(f"I| Conta: {self.conta}")
        print(f"I| Agência: {self.agencia}")
        print(f"I| Saldo: R${self.saldo}")       