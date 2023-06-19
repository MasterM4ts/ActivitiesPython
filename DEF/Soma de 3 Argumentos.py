#Programa que Efetua a Soma de 3 Argumentos informados pelo Usuário.

def soma(x,y,z):
    soma_arg = x + y + z
    return soma_arg

print("+"+"="*25+"+")
num_1 = float(input("I| Digite o 1º Número:\n>> "))
num_2 = float(input("I| Digite o 2º Número:\n>> "))
num_3 = float(input("I| Digite o 3º Número:\n>> "))
result = soma(num_1,num_2,num_3)
print("-"*20)
print("I| Resultado: %.2f"%result)
print("="*25)