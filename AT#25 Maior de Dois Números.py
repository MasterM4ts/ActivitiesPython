#Programa que Imprime o Maior dos 2 Números Informados pelo Usúario.
print("+"+"="*35+"+")
num_1 = float(input("I| Digite um Valor: \n>> "))
num_2 = float(input("I| Digite outro Valor: \n>> "))

if num_1 > num_2:
    print("+"+"="*35+"+")
    print("I| O Número Maior: %.2f"%num_1)
    print("+"+"="*35+"+")
elif num_1 < num_2:
    print("+"+"="*35+"+")
    print("I| O Número Maior: %.2f"%num_2)
    print("+"+"="*35+"+")
else:
    print("+"+"="*35+"+")
    print("I| Os Números são Iguais.")
    print("+"+"="*35+"+")