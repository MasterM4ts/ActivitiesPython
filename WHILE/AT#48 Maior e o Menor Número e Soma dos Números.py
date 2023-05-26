#Programa que Determina o Maior e o Menor Número Digitado pelo Usúario e Efetua a Soma dos Números.

list_num = []

while True:
    print("+"+"="*35+"+")
    num = input("I| Digite um Número ou \"x\" para Sair:\n>> ")
    print("+"+"="*35+"+")
    
    if num == "x":
        break
    
    num = int(num)
    list_num.append(num)
    
if num == "x":
    
    if len(list_num)!=0:
        
        print("+"+"="*35+"+")
        print("I| Maior Número:",max(list_num))
        print("I| Menor Número:",min(list_num))
        print("I| Soma dos Números:",sum(list_num))
        print("+"+"="*35+"+")
        print("I| Programa Encerrado")
        print("+"+"="*35+"+")