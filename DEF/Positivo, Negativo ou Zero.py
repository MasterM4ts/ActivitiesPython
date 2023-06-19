#Programa que Informa se o Número é Positivo, Negativo ou Zero.

def calculo(x):
    if x > 0:
        return True
    else:
        return False

x = float(input("I| Digite um Número:\n>> "))
if x == 0:
    print("-"*20)
    print("I| O Número é Zero (\"Zero\").")
elif calculo(x):
    print("-"*20)
    print("I| O Número %.2f é Positivo (\"P\")."%x)
else:
    print("-"*20)
    print("I| O Número %.2f é Negativo (\"N\")."%x)
print("="*25)