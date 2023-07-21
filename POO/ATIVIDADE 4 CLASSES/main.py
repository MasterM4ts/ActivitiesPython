from Cadastro import*
from Banco import*
from Cartao import*
from Compra import*
from pwinput import*


print("+"+"="*20+"+")
print("I| Cadastro Usuário I|")
nome = input("I| Digite seu Nome:\n>> ")
cpf = input("I| Digite seu CPF:\n>> ")
telefone = input("I| Digite seu Telefone:\n>> ")
email = input("I| Digite seu Email:\n>> ")
endereco = input("I| Digite seu Endereço:\n>> ")
senha = pwinput("I| Crie uma Senha:\n>> ")
Cadastro(nome,cpf,telefone,email,endereco,senha)
print("I| Cadastro Realizado I|")
os.system("pause")
os.system("cls")


while True:
    print("+"+"="*16+"+")
    menu = input("I| Digite a Opção:\n(1) >> Acesso de Conta Banco\n(2) >> Acesso ao App do Cartao\n(0) >> Encerrar Programa\n>> ")
    os.system("cls")

    
    if menu == "1":
        verdade = False
        while True:
            print("I| \"Bem Vindo\" Ao Banco I|")
            print("-"*28)
            inicio = input("I| Escolha uma Opção:\n(1) >> Cadastro\n(2) >> Depositar\n(3) >> Sacar\n(4) >> Relatório\n(0) >> Sair do Banco\n>> ")
            os.system("cls")
            

            if inicio == "1":
                print("I| Cadastro Banco I|")
                Banco.cadastro()
                verdade = True
                print("I| Cadastro Realizado I|")
                os.system("pause")
                os.system("cls")
            

            if verdade is True:

                if inicio == "2":
                    while True:
                        try:
                            valor = float(input("I| Digite o Valor que Deseja Depositar:\n>> "))
                        

                        except ValueError:
                            print("-"*28)
                            print("I| Digite Somente Números I|")
                            print("-"*28)
                        

                        else:
                            Banco.depositar(valor)
                
                
                elif inicio == "3":
                    senha = input("I| Digite sua Senha:\n>> ")
                    print(f"I| Saldo...{Banco.sacar(senha)}")
                    os.system("pause")
                    os.system("cls")
                
                
                elif inicio == "4":
                    senha = input("I| Digite sua Senha:\n>> ")
                    Banco.relatorio(senha)
                
                
                elif inicio == "0":
                    break
            
            else:
                print("-"*46)
                print("I| Realize um Cadastro para Acessar o Banco I|")
                print("-"*46)
                os.system("pause")
                os.system("cls")


    elif menu == "2":
        verdade = False
        while True:
            print("I| \"Bem Vindo\" Ao App do Cartão I|")
            print("-"*28)
            inicio = input("I| Ecolha uma Opção:\n(1) >> Cadastro\n(2) >> Depositar\n(3) >> Sacar\n(4) >> Comprar\n(0) >> Sair do App do Cartão\n>> ")
            os.system("cls")

            
            if inicio == "1":
                print("I| Cadastro de Cartão I|")
                Cartao.cadastro()
                verdade = True
                print("I| Cadastro Realizado I|")
                os.system("pause")
                os.system("cls")
            
            if verdade is True:
                if inicio == "2":


                    while True:
                        try:
                            print("-"*39)
                            valor = float(input("I| Digite o Valor que Deseja Depositar:\n>> "))
                        

                        except ValueError:
                            print("-"*28)
                            print("I| Digite Somente Números I|")
                            print("-"*28)
                        

                        else:
                            Banco.depositar()
                
                
                elif inicio == "3":
                    senha = pwinput("I| Digite sua Senha:\n>> ")
                    print(f"I| Saldo...{Banco.sacar(senha)}")
                    os.system("pause")
                    os.system("cls")
                
                
                elif inicio == "4":
                        print("-"*39)
                        produto = input("I| Digite o Produto que Deseja Comprar:\n>> ")


                        while True:
                            try:
                                valor = float(input("I| Digite o Valor do Produto:\n>> "))
                            

                            except ValueError:
                                print("-"*28)
                                print("I| Digite Somente Números I|")
                                print("-"*28)
                            

                            else:
                                Compra.comprar(produto,valor)
                                break
            

            else:
                print("-"*54)
                print("I| Realize um Cadastro para Acessar o App do Cartão I|")
                print("-"*54)
                os.system("pause")
                os.system("cls")

    
    elif menu == "0":
        print("-"*37)
        print("I| \"Obrigado por Utilizar o Programa\"\nI| \"Volte Sempre\"")
        print("-"*37)
        break
    

    else:
        print("-"*20)
        print("I| Opção Invalida I|")
        print("-"*20)
        os.system("pause")
        os.system("cls")