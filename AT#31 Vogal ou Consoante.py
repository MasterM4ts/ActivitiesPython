#Programa que Informa se a Letra Digita é uma Vogal ou Consoante.

print("+"+"="*35+"+")
letra = input("I| Digite uma Letra: \n>> ")
letra = letra.upper()

if letra == "A" or letra == "E"  or letra == "I" or letra == "O" or letra == "U":
    print("="*5)
    print("I| Sua Letra",letra[0:1],"é uma Vogal.")
    print("+"+"="*35+"+")
else:
    print("="*5)
    print("I| Sua Letra",letra[0:1],"é uma Consoante.")
    print("+"+"="*35+"+")