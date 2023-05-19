#Programa que Conta Quantas Vezes se pode Reduzir em 1 o Valor do Número Digitado pelo Usúario.print 
print("+"+"="*35+"+")
num = int(input("I| Digite um Valor: "))

while num != 0:
    num += - 1
    print(">>",num)
print("+"+"="*35+"+")