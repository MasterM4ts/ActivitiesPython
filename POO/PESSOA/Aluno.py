#Herença#
from Pessoa import*
class Aluno(Pessoa):
    

    def __init__(self, mensalidade, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.mensalidade = mensalidade
        print("-"*33)
        print("I| Seja Bem-Vindo querio Aluno I|")
        super().relatorio()
        print(f"I| Mensalidade...{self.mensalidade}")
        print("-"*33)