from Cadastro import*
class Banco(Cadastro):


    def __init__(self, nome, cpf, telefone, email, endereco, senha):
        super().__init__(nome, cpf, telefone, email, endereco, senha)
        self.__saldo = 0
        

    def cadastro():
        nome = input("I| Digite seu Nome:\n>> ")
        cpf = input("I| Digite seu CPF:\n>> ")
        fone = input("I| Digite seu Telefone:\n>> ")
        email = input("I| Digite seu Email:\n>> ")
        endereco = input("I| Digite seu Endereço:\n>> ")
        senha = pwinput("I| Crie uma Senha:\n>> ")
        Banco(nome,cpf,fone,email,endereco,senha) 
        return True  


    def depositar(self,valor):
        self.__saldo += valor
        print("I| Deposito Concluido I|")
        os.system("pause")
        os.system("cls")
    

    def sacar(self,senha):
        if senha == self.__senha:
            
            
            while True:
                try:
                    valor = float(input("I| Digite o Valor a ser Sacado:\n>> "))


                except ValueError:
                    print("-"*28)
                    print("I| Digite Somente Números I|")
                    print("-"*28)
                
                
                else:
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
