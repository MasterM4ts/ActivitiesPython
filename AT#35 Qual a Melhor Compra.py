#Programa que Informa Qual a Melhor Compra Deve ser Feita.  //Mais Barato.

print("+"+"="*35+"+")
nomepro_1 = input("I| Digite o Nome do 1º Produto: \n>> ")
produto_1 = float(input("I| Digite o Preço do 1° Produto: \n>> "))

nomepro_2 = input("I| Digite o Nome do 2º Produto: \n>> ")
produto_2 = float(input("I| Digite o Preço do 2° Produto: \n>> "))

nomepro_3 = input("I| Digite o Nome do 3º Produto: \n>> ")
produto_3 = float(input("I| Digite o Preço do 3° Produto: \n>> "))


if produto_1 < produto_2 and produto_1 < produto_3:
    print("+"+"="*60+"+")
    print("I| O Produto %s,Custando R$%.2f é o Mais Custo Benefício"%(nomepro_1.capitalize(),produto_1))
    print("+"+"="*60+"+")

elif produto_2 < produto_1 and produto_2 < produto_3:
    print("+"+"="*60+"+")
    print("I| O Produto %s,Custando R$%.2f é o Mais Custo Benefício"%(nomepro_2.capitalize(),produto_2))
    print("+"+"="*60+"+")

else:
    print("+"+"="*60+"+")
    print("I| O Produto %s,Custando R$%.2f é o Mais Custo Benefício"%(nomepro_3.capitalize(),produto_3))
    print("+"+"="*60+"+")