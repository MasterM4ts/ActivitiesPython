#Programa Calculadora.

operacao = 1
while operacao != 0:
    import os
    print("+"+"="*35+"+")
    print("Bem vindo a Calculadora")
    print("+"+"="*35+"+")
    print("I| 1 >> Adição"+" "*20+"|")
    print("I| 2 >> Subtração"+" "*17+"|")
    print("I| 3 >> Multiplicação"+" "*13+"|")
    print("I| 4 >> Divisão"+" "*19+"|")
    print("I| 5 >> Raiz Quadrada"+" "*13+"|")
    print("I| 6 >> Exponenciação"+" "*13+"|")
    print("I| 7 >> Volume de um Cubo"+" "*9+"|")
    print("I| 8 >> Área de um Quadrado"+" "*7+"|")
    print("I| 9 >> Média de 4 Números"+" "*8+"|")
    print("I| 10 >> Fatorial"+" "*17+"|")
    print("I| 0 >> Sair Calculadora"+" "*10+"|")
    print("+"+"="*35+"+")
    operacao = int(input("I| Digite a Operação Desejada: \n>> "))

    if operacao == 1:
        print("+"+"-"*35+"+")
        print("Bem vindo a Adição")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite o 1º Número: \n>> "))
        num_2 = float(input("I| Digite o 2º Número: \n>> "))
        result = num_1 + num_2
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(" %.0f + %.0f "%(num_1,num_2))
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 2:
        print("+"+"-"*35+"+")
        print("Bem vindo a Subtração")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite o 1º Número: \n>> "))
        num_2 = float(input("I| Digite o 2º Número: \n>> "))
        result = num_1 - num_2
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(" %.0f - %.0f "%(num_1,num_2))
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 3:
        print("+"+"-"*35+"+")
        print("Bem vindo a Multiplicação")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite o 1º Número: \n>> "))
        num_2 = float(input("I| Digite o 2º Número: \n>> "))
        result = num_1 * num_2
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(" %.0f X %.0f "%(num_1,num_2))
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 4:
        print("+"+"-"*35+"+")
        print("Bem vindo a Divisão")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite o 1º Número: \n>> "))
        num_2 = float(input("I| Digite o 2º Número: \n>> "))
        result = num_1 / num_2
        print("+"+"-"*35+"+"),
        print("Resultado: ") 
        print(" %.0f "%num_1)
        print("-"*5)
        print(" %.0f "%num_2)
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 5:
        print("+"+"-"*35+"+")
        print("Bem vindo a Raiz Quadrada")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite o um Número: \n>> "))
        result = (num_1 ** 1/2)
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(" %.0f "%num_1)
        print("-"*5)
        print(" 1/2 ")
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 6:
        print("+"+"-"*35+"+")
        print("Bem vindo a Exponenciação")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite o um Número: \n>> "))
        result = num_1 ** num_1
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(" %.0f ^ %.0f"%(num_1,num_1))
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 7:
        print("+"+"-"*35+"+")
        print("Bem vindo a Volume de um Cubo")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite o Comprimento da Aresta: \n>> "))
        result = num_1 ** 3
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(" %.0f ^ 3"%num_1)
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 8:
        print("+"+"-"*35+"+")
        print("Bem vindo a Área de um Quadrado")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite um Lado do Quadrado: \n>> "))
        result = num_1 ** 2
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(" %.0f ^ 2"%num_1)
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 9:
        print("+"+"-"*35+"+")
        print("Bem vindo a Média de 4 Números")
        print("+"+"-"*35+"+")
        num_1 = float(input("I| Digite o 1º Número: \n>> "))
        num_2 = float(input("I| Digite o 2º Número: \n>> "))
        num_3 = float(input("I| Digite o 3º Número: \n>> "))
        num_4 = float(input("I| Digite o 4º Número: \n>> "))
        result = (num_1 + num_2 + num_3 + num_4) / 4 
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(" %.0f + %.0f + %.0f + %.0f "%(num_1,num_2,num_3,num_4))
        print("-"*20)
        print(" "*9+"4")
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    elif operacao == 10:
        print("+"+"-"*35+"+")
        print("Bem vindo a Fatorial")
        print("+"+"-"*35+"+")
        num_1 = int(input("I| Digite o um Número: \n>> "))
        result = 1
        count = 1
        while count <= num_1:
            result *= count
            count += 1
        print("+"+"-"*35+"+")
        print("Resultado: ") 
        print(">> %.0f <<"%result)
        print("+"+"-"*35+"+")

    else:
        break

    os.system("pause")
    os.system("cls")