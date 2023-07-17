#Herença#
from Pessoa import*
class Professor(Pessoa):
    

    def __init__(self, salario, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.salario = salario
        print("-"*30)
        print("I| Seja Bem-Vindo Professor I|")
        super().relatorio()
        print(f"I| Salario...{self.salario}")
        print("-"*30)