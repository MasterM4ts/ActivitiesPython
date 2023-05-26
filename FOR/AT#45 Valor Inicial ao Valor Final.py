#Programa Imprime do Valor Inicial ao Valor Final e Efetua a Soma dos Números Digitado Pelo Usuário.

print("+"+"="*35+"+")
num_1 = int(input("I| Digite um Valor: \n>> "))
num_2 = int(input("I| Digite um outro Valor: \n>> "))
print("+"+"="*35+"+")

num_2+=1
soma = []

for num_1 in range(num_2):
    print(num_1)
    soma.append(num_1)

print("+"+"="*35+"+")
print("I| Soma dos Números: ",sum(soma))
print("+"+"="*35+"+")