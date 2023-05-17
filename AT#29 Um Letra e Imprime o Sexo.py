#Programa que Verifica uma Letra Digitada e Imprime o Sexo.

print("+"+"="*35+"+")
sexo = input("I| Digite uma Letra do Seu Sexo:  \nI| M \nI| F \nI| O \n>> ")
sexo = sexo.upper()

if sexo == "M":
    print("+"+"="*35+"+")
    print("I| M = Masculino.")
elif sexo == "F":
    print("+"+"="*35+"+")
    print("I| F = Feminino.")
elif sexo == "O":
    print("+"+"="*35+"+")
    print("I| O = Outros.")
else:
    print("+"+"="*35+"+")
    print("I| Sexo Invalido.")