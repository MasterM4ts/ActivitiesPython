#Programa que lê 5 Números e Informa a Soma e a Média dos Números.

soma = []

for x in range(0,5):
    print("+"+"="*35+"+")
    num = float(input("I| Digite um Número: \n>> "))
    soma.append(num)

soma = sum(soma)
media = soma /5
print("+"+"="*37+"+")
print("I| Soma dos Números: %.2f "%soma)
print("I| Média dos Números: %.2f "%media,)
print("+"+"="*37+"+")