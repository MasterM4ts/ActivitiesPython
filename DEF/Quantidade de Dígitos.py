#Programa que Informa a Quantidade de Dígitos de um Número Inteiro Digitado pelo Usuário.

def qtd_digitos(num):
    num = str(num)
    for i in num:
        cont += 1 
    return cont
print("+"+"="*72+"+")
print("I| OBS: Digite um Número e o Programa Retornara a Quantidade de Dígitos.")
print("-"*28)
num = int(input("I| Digite um Número Inteiro:\n>> "))
qtd_digitos(num)
print(f"I| Quantidade de Dígitos: {qtd_digitos(num)}")
print("="*30)