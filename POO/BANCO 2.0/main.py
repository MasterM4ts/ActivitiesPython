from Banco import*
import os

while True:


    print("="*27)
    print("I|   \"Cadatro de Banco\"  I|")
    print("-"*27)
    print("I| Informe os Dados Abaixo:\n")
    nome = input("I| Digite seu Nome:\n>> ")
    cpf = input("I| Digite seu CPF:\n>> ")
    senha = input("I| Digite sua Senha:\n>> ")
    banco = Banco(nome,cpf,senha)
    os.system("pause")
    os.system("cls")
    break
    

menu = 1
while True:


    print("+"+"="*23+"+")
    menu = input("I| Digite uma das Opções:\n(1) >> Depositar\n(2) >> Sacar\n(3) >> Extrato\n(0) >> Sair\n>> ")


    if menu == "1":
        print("-"*15)
        print("I| Depositar I|")
        valor = float(input("I| Digite o Valor que Deseja Depositar:\n>> "))
        banco.depositar(valor)
        print("-"*15)
        os.system("pause")
        os.system("cls")

    
    if menu == "2":
        print("-"*11)
        print("I| Sacar I|")
        senha = input("I| Digite sua Senha:\n>> ")
        print(f"I| Saldo de R$ {banco.sacar(senha)}")
        print("-"*11)
        os.system("pause")
        os.system("cls")

    
    if menu == "3":
        print("-"*13)
        print("I| Extrato I|")
        senha = input("I| Digite sua Senha:\n>> ")
        banco.extrato(senha)
        print("-"*13)
        os.system("pause")
        os.system("cls")
    

    elif menu == "0":
        print("I| \"Obrigado por Utilizar o Programa\"\nI| \"Volte Sempre\"")
        print("-"*42)
        break
    

    else:
        print("-"*20)
        print("I| Opção Invalida I|")
        print("-"*20)
        os.system("pause")
        os.system("cls")