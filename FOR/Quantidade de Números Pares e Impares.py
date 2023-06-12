#Programa que pede 10 Números e Informa a Quantidade de Números Pares e Impares.

pares = 0
impares = 0
for i in range(0,10):
    print("-"*35)
    num = int(input("I| Digite um Número Inteiro:\n>> "))

    if num%2 == 0:
        pares += 1
    
    else:
        impares += 1

print("+"+"="*35+"+")
print("I|"+" "*10+">>RESULTADO<<"+" "*10+"|I")  
print("-"*37)    
print("I| Números Pares: %d"%pares)
print("I| Números Impares: %d"%impares)
print("="*37)