print("+"+"="*35+"+")
a = int(input("I| Qual a População do País A: \n>> "))
while a < 0:
    a = int(input("I| A População do País A Deve ser Maior que 0: \n>> "))
taxa_A = float(input("I| Qual a Taxa de Crecimento do País A: \n>> "))

b = int(input("I| Qual a População do País B: \n>> "))
while b < 0:
    b = int(input("I| A População do País B Deve ser Maior que 0: \n>> "))
taxa_B = float(input("I| Qual a Taxa de Crecimento do País B: \n>> "))

ano = 0
while a < b:
    ano += 1
    a = int((1 + (taxa_A/100)) * a)
    b = int((1 + (taxa_B/100)) * b)
    print("I| Anos>: %d"%ano)
    print("I| População A: %d"%a)
    print("I| População B: %d"%b)

print("Ultrapassa no Ano: %d"%ano)