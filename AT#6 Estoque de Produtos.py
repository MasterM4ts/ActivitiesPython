#Programa para ler Nome do Produto,Quantidade Comprada,o Valor Unitário e o Porcentual de Desconto.
#Após ler ,Calcular o Valor Total. 
print("-"*30)
name_Produto = input("Digite o Nome do Produto: \n>> ")
quantidade_Produto = int(input("Digite a Quantidade de Produtos: \n>> "))
valor_Uni = float(input("Digite o Valor Unitário Do Produto: \n>> "))
desconto_Produto = float(input("Digite o Porcentual de Desconto do Produto: \n>> "))

valor_Total = quantidade_Produto * valor_Uni
valor_Total = valor_Total - desconto_Produto

print("+"+"="*26+"+")
print(" "*7 + "<Nota Fiscal>")
print("-"*27)
print("I| Nome do Produto: %s."%name_Produto)
print("-"*27)
print("I| Valor Total: R$%.2f"%valor_Total)
print("+"+"="*26+"+")