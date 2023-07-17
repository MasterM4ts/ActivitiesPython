from Cadastro import*
class Banco(Cadastro):


    def __init__(self, nome, cpf, telefone, email, endereco, senha):
        super().__init__(nome, cpf, telefone, email, endereco, senha)
        self.__saldo = 0
        

    def cadastro(self):
        return super().cadastro()


    def depositar(self,valor):
        self.__saldo += valor
        print("I| Deposito Concluido I|")
    

    def sacar(self,senha):
        if senha == self.__senha:
            valor = float(input("I| Digite o Valor a ser Sacado:\n>> "))
            self.__saldo -= valor
            return self.__saldo
        else:
            print("I| Senha Invalida I|")
            os.system("pause")
            os.system("cls")


    def relatorio(self,senha):
        if senha == self.__senha:
            print(f"I| Nome...{self.nome}")
            print(f"I| Telefone...{self.telefone}")
            print(f"I| Email...{self.email}")
            print(f"I| Endereço...{self.endereco}")
            print(f"I| Saldo...{self.__saldo}")
            os.system("pause")
            os.system("cls")
        else:
            print("I| Senha Invalida I|")
            os.system("pause")
            os.system("cls")
