#Programa que Informa o Maior Número Digitado pelo Usúario.

print("+"+"="*35+"+")
num_1 = int(input("I| Digite um Número: \n>> "))
num_2 = int(input("I| Digite um 2º Número: \n>> "))
num_3 = int(input("I| Digite um 3º Número: \n>> "))

lista = [num_1,num_2,num_3]

print("+"+"="*35+"+")
print("I| O Maior Número Digitado Foi: ",max(lista))
print("+"+"="*35+"+")