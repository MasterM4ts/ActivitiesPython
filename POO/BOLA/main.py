from Bola import*
import os

while True:

    
    try:
        print("="*22)
        print("I| Cadastro da Bola I|")
        print("-"*22)
        cor = input("I| Digite a Cor da Bola:\n>> ")
        material = input("I| Digite o Material da Bola:\n>> ")
        marca = input("I| Digite a Marca da Bola:\n>> ")
        circunferencia = float(input("I| Digite a Circunferência:\n>> "))


    except ValueError:
        print("I| Erro | Tente Novamente")
        print("I| Digite Somente Números.")
        os.system("pause")
        os.system("cls") 


    else:
        break


while True:
    

    bola = Bola(cor,circunferencia,material,marca)
    menu = input("I| Digite uma Opção:\n(1) >> Mudar Cor da Bola\n(2) >> Mostrar Bola\n(0) >> Sair.\n>> ")


    if menu == "1":
        print("-"*42)
        alt_cor = input("I| Para Qual Cor deseja Alterar sua Bola: ")
        bola.troca_Cor(alt_cor)
        os.system("pause")
        os.system("cls")
    

    elif menu == "2":
        print("-"*10)
        print("I| Bola I|")
        bola.mostra_Bola()       
        os.system("pause")
        os.system("cls")
    

    elif menu == "0":
        print("I| \"Obrigado por Utilizar o Programa\"\nI| \"Volte Sempre\"")
        print("-"*42)
        break


    else:
        print("-"*20)
        print("I| Opção Invalida I|")
        os.system("pause")
        os.system("cls")