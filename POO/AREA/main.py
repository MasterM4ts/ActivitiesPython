from Area import*
import os


while True:

    
    try:
        print("="*32)
        print("I|   \"Área de Um Quadrado\"  I|")
        print("-"*32)
        lado = float(input("I| Digite um Lado do Quadrado:\n>> "))
        area = Area(lado)     
    
    except ValueError:
        print("-"*42)
        print("I| Erro | Digite Apenas Números")
        print("-"*42)
        os.system("pause")
        os.system("cls")
    
    
    else:
        break


menu = 1
while True:


    print("+"+"="*23+"+")
    menu = input("I| Digite uma das Opções:\n(1) >> Mostrar Área do Quadrado\n(2) >> Mudar Valor do Lado\n(0) >> Sair\n>> ")
    

    if menu == "1":
        print("-"*18)
        print("I| Mostrar Área I|")
        print(f"I| Área: {area.mostrar_area(lado)}")
        print("-"*18)
        os.system("pause")
        os.system("cls")
    

    elif menu == "2":
        print("-"*14)
        print("I| Mudar Valor do Lado I|")
        lado = float(input("I| Digite o Valor do Lado:\n>> "))
        print(f"I| Lado: {lado}")
        print(f"I| Área: {area.mudar_valor_lado(lado)}")
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