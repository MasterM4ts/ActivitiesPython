#Programa que Informa se o Número é Positivo,Negativo ou Neutro.
print("+"+"="*35+"+")
num = int(input("Digite um Valor: \n>> "))

if num > 0:
    print("+"+"="*35+"+")
    print("I| Seu Número é Positivo.")
    print("+"+"="*35+"+")
elif num < 0:
    print("+"+"="*35+"+")
    print("I| Seu Número é Negativo.")
    print("+"+"="*35+"+")
else:
    print("+"+"="*35+"+")
    print("I| Seu Número é Neutro.")
    print("+"+"="*35+"+")