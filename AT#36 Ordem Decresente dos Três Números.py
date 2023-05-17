#Programa que Informa a Ordem Decresente dos Três Números Digitados pelo Usúario.

print("+"+"="*35+"+")
num_1 = int(input("I| Digite o 1º Número: \n>> "))
num_2 = int(input("I| Digite o 2º Número: \n>> "))
num_3 = int(input("I| Digite o 3º Número: \n>> "))

lista = [num_1,num_2,num_3]
lista.sort(reverse=True)

print("+"+"="*40+"+")
print("I| Ordem Decresente dos Números:",lista)
print("+"+"="*40+"+")