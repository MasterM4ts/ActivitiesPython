from Retangulo import*
import os

while True:

    
    try:
        print("="*27)
        print("I|   \"Calculos de Retângulo\"  I|")
        print("-"*27)
        base = float(input("I| Digite a Base do Seu Retângulo:\n>> "))
        altura = float(input("I| Digite a Altura do Seu Retângulo:\n>> "))
        retangulo = Retangulo(base,altura)
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
    menu = input('''I| Digite uma das Opções:\n(1) >> Mostrar Informações Sobre o Retângulo.\n(2) >> Mostrar Área do Retângulo.\n
    (3) >> Mostrar Perimetro do Retângulo.\n(4) >> Mostrar Rodapé do Retângulo.\n(5) >> Alterar Lados.\n
    (0) >> Sair\n>> ''')
    
    if menu == "1":
        print("-"*35)
        print("I| Informações Sobre o Retângulo I|")
        retangulo.mostrar_info_retangulo(base,altura)
        print("-"*35)
        os.system("pause")
        os.system("cls")
    

    elif menu == "2":
        print("-"*31)
        print("I| Mostrar Área do Retângulo I|")
        retangulo.mostrar_area(base,altura)
        print("-"*31)
        os.system("pause")
        os.system("cls")
    

    elif menu == "3":
        print("-"*36)
        print("I| Mostrar Perimetro do Retângulo I|")
        retangulo.mostrar_perimetro(base,altura)
        print("-"*36)
        os.system("pause")
        os.system("cls")


    elif menu == "4":
        print("-"*33)
        print("I| Mostrar Rodapé do Retângulo I|")
        retangulo.mostrar_rodape(retangulo.mostrar_area(base,altura))
        print("-"*33)
        os.system("pause")
        os.system("cls")


    elif menu == "5":
        print("-"*19)
        print("I| Alterar Lados I|")
        base = float(input("I| Digite a Base do Seu Retângulo:\n>> "))
        altura = float(input("I| Digite a Altura do Seu Retângulo:\n>> "))
        print("-"*19)
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