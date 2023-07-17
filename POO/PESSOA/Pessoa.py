#Herença#
class Pessoa:


    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome = nome
        self.idade =idade
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado

    
    def relatorio(self):
        print(f"I| Nome...{self.nome}")
        print(f"I| Idade...{self.idade}")
        print(f"I| Endereço...{self.endereco}")
        print(f"I| Cidade...{self.cidade}")
        print(f"I| Estado...{self.estado}")