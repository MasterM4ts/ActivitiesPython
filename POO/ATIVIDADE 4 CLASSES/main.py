from Cadastro import*
from Banco import*
from Cartao import*
from Compra import*
from pwinput import*

print("I| Cadastro Usuário I|")
nome = input("I| Digite seu Nome:\n>> ")
cpf = input("I| Digite seu CPF:\n>> ")
telefone = input("I| Digite seu Telefone:\n>> ")
email = input("I| Digite seu Email:\n>> ")
endereco = input("I| Digite seu Endereço:\n>> ")
senha = pwinput("I| Crie uma Senha:\n>> ")
Cadastro(nome,cpf,telefone,email,endereco,senha)
Banco(nome,cpf,telefone,email,endereco,senha)
Cartao(nome,cpf,telefone,email,endereco,senha,cartao="0")
Compra(nome, cpf, telefone, email, endereco, senha)


while True:
    menu = input("I| Digite a Opção:\n(1) >> Cadastro de Conta Banco\n(2) >> Cadastro de Cartao\n(0) >> Encerrar Programa")

    
    if menu == "1":
        print("I| Cadastro Banco I|")
        Banco.cadastro()
        
        
        while True:
            print("I| \"Bem Vindo\" Ao Banco I|")
            print("-"*28)
            inicio = input("I| Ecolha uma Opção:\n(1) >> Depositar\n(2) >> Sacar\n(3) >> Relatório\n(0) >> Sair do Banco\n>> ")
            
            
            if inicio == "1":
                valor = float(input("I| Digite o Valor que Deseja Depositar:\n>> "))
                Banco.depositar()
            
            
            elif inicio == "2":
                senha = input("I| Digite sua Senha:\n>> ")
                print(f"I| Saldo...{Banco.sacar(senha)}")
            
            
            elif inicio == "3":
                senha = input("I| Digite sua Senha:\n>> ")
                Banco.relatorio(senha)
            
            
            elif inicio == "0":
                break


    elif menu == "2":
        print("I| Cadastro de Cartão I|")
        Cartao.cadastro()



        while True:
            print("I| \"Bem Vindo\" Ao App do Cartão I|")
            print("-"*28)
            inicio = input("I| Ecolha uma Opção:\n(1) >> Depositar\n(2) >> Sacar\n(3) >> Comprar\n(0) >> Sair do App do Cartão\n>> ")
            
            
            if inicio == "1":
                valor = float(input("I| Digite o Valor que Deseja Depositar:\n>> "))
                Banco.depositar()
            
            
            elif inicio == "2":
                senha = pwinput("I| Digite sua Senha:\n>> ")
                print(f"I| Saldo...{Banco.sacar(senha)}")
            
            
            elif inicio == "3":
                add_compra = input("I| Escolha um Opção:\n(1) >> Adicionar Produto ao Carrinho\n(2) >> Comprar\n>> ")
                
                
                if add_compra == "1":
                    produto = input("I| Digite o Produto de Deseja Comprar:\n>> ")
                    valor = float(input("I| Digite o Valor do Produto:\n>> "))
                    Compra.carrrinho(produto,valor)
                

                else:
                    Compra.comprar()
            
            
            elif inicio == "0":
                break

    
    elif menu == "0":
        print("-"*5)
        print("I| \"Obrigado por Utilizar o Programa\"\nI| \"Volte Sempre\"")
        print("-"*42)
        break
    

    else:
        print("-"*20)
        print("I| Opção Invalida I|")
        print("-"*20)
        os.system("pause")
        os.system("cls")