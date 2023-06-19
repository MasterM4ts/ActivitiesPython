#Programa que Solicita 2 Números ao Usuário e uma Função Efetua o Calculo.

def soma(x,y):
    result = x + y
    return result

a = int(input("I| Digite o 1º Número:\n>> "))
b = int(input("I| Digite o 2º Número:\n>> "))
res = soma(a,b)
print("Soma:",res)