#Programa que Converte da Notação de 24 Horas para a Notação de 12 Horas.

import os
def converter(horas,minutos):
        if horas > 12:
            horas -= 12
            minutos = str(minutos)
            ajusteMin = len(minutos)
            if ajusteMin == "1":
                print(f"I| Conversão da Notação: {horas}:0{minutos} P.M")
            else:
                print(f"I| Conversão da Notação: {horas}:{minutos} A.M")
        else:
            minutos = str(minutos)
            ajusteMin = len(minutos)
            if ajusteMin == "1":
                print(f"I| Conversão da Notação: {horas}:0{minutos} A.M")
            else:
                print(f"I| Conversão da Notação: {horas}:{minutos} A.M")

inicio = 1
while inicio != 0:
    while True:
        try:
            print("="*35)
            inicio = int(input("I| DIGITE:\n1 >> Iniciar Converção de Notação.\n0 >> Encerrar Programa.\n>> "))
            
        except ValueError:
            print("-"*27)
            print("I| \"Erro\" Valor Invalido\nI| \"Tente Novamente\"")
            print("-"*27)
            os.system("pause")
            os.system("cls")
        else:
            break  
    if inicio == 1:
        while True:
            try:
                horas = int(input("I| Digite Que Horas são:\n>> "))
                minutos = int(input("I| Digite os Minutos:\n>> "))
                print("-"*34)
                converter(horas,minutos)
                os.system("pause")
                os.system("cls")

            except ValueError:
                print("-"*27)
                print("I| \"Erro\" Valor Invalido\nI| \"Tente Novamente\"")
                print("-"*27)
                os.system("pause")
                os.system("cls")
            else:
                break