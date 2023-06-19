#Programa que Verifica se o Número é Par ou Impar Utilizando uma Função.

def par(x):
    if (x%2) == 0:
        return True
    else:
        return False

while True:
    num = float(input("I| Digite um Número:\n>> "))
    if par(num):
        print("I| È Par.")
    else:
        print("I| È Impar.")