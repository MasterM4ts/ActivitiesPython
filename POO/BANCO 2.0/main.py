#Encapsulamento#
from Banco import*
from pwinput import*
import os


while True:
    print("="*33)
    print("I|   \"Cadatro de Conta Banco\"  I|")
    print("="*33)
    print("I| Informe os Dados Abaixo:\n")
    nome = input("I| Digite seu Nome:\n>> ")
    cpf = input("I| Digite seu CPF:\n>> ")
    senha = pwinput("I| Crie sua Senha:\n>> ")
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
        print("-"*15)
        
        
        while True:
            try:
                valor = float(input("I| Digite o Valor que Deseja Depositar:\n>> "))
            
            
            except ValueError:
                print("-"*27)
                print("I| Digite Ápenas Números I|")
                print("-"*27)
            
            
            else:
                banco.depositar(valor)
                os.system("pause")
                os.system("cls")
                break

    
    elif menu == "2":
        print("-"*11)
        print("I| Sacar I|")
        print("-"*11)
        print("I| Esqueceu Senha? Digite >>\"X01\"<<")
        senha = pwinput("I| Digite sua Senha:\n>> ")


        if senha == "X01":
            esc_senha = input("I| Digite seu CPF:\n>> ")
            banco.esc_senha(esc_senha)


        print(f"I| Saldo de R$ {banco.sacar(senha)}")
        os.system("pause")
        os.system("cls")

    
    elif menu == "3":
        print("-"*13)
        print("I| Extrato I|")
        print("-"*13)
        print("I| Esqueceu Senha? Digite >>\"X01\"<<")
        senha = pwinput("I| Digite sua Senha:\n>> ")
        
        
        if senha == "X01":
            esc_senha = input("I| Digite seu CPF:\n>> ")
            banco.esc_senha(esc_senha)
        
        
        banco.extrato(senha)
        print("-"*26)
        os.system("pause")
        os.system("cls")
    

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