#Abstração#
from Conta import*
import os

while True:

    
    try:
        print("="*27)
        print("I|   \"Cadatro de Banco\"  I|")
        print("-"*27)
        print("I| Informe os Dados Abaixo:\n")
        nome = input("I| Digite seu Nome:\n>> ")
        conta = input("I| Informe sua Conta:\n>> ")
        agencia = int(input("I| Digite sua Agência:\n>> "))
        cpf = input("I| Digite seu CPF:\n>> ")
        fone = input("I| Digite seu Telefone:\n>> ")
        banco = Conta(nome,conta,agencia,cpf,fone)
        os.system("pause")
        os.system("cls")
    
    
    except ValueError:
        print("-"*42)
        print("I| Erro | Dado Informado de Maneira Errada")
        print("-"*42)
        os.system("pause")
        os.system("cls")
    
    
    else:
        break
    

menu = 1
while True:


    print("+"+"="*23+"+")
    menu = input("I| Digite uma das Opções:\n(1) >> Saque\n(2) >> Deposito\n(3) >> Extrato\n(0) >> Sair\n>> ")
    

    if menu == "1":
        print("-"*11)
        print("I| Saque I|")
        dinheiro = float(input("I| Digite a Quantia do Saque:\n>> "))
        banco.saque(dinheiro)
        print("-"*11)
        os.system("pause")
        os.system("cls")
    

    elif menu == "2":
        print("-"*14)
        print("I| Deposito I|")
        print("I| Depositos Acima de R$5000 Será Revisado Pelo Banco.")
        dinheiro = float(input("I| Digite a Quantia do Deposito:\n>> "))
        banco.deposito(dinheiro)
        print("-"*14)
        os.system("pause")
        os.system("cls")
    

    elif menu == "3":
        print("-"*14)
        print("I| Extrato I|")
        banco.extrato()
        print("-"*14)
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