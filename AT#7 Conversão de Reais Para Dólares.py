#Sistema Para Converter valor em Reais para Dólares.
print("+"+"-"*26+"+")
reais = float(input("Digite a Quantia em Reais: \n>> "))
dolares = float(input("Digite o Valor da Cotação do Dólar: \n>> "))
print("+"+"-"*26+"+")

dolares = reais / dolares

print("I| Reais: R$%.2f"%reais)
print("I| Dólares: $%.2f"%dolares)
print("+"+"-"*26+"+")