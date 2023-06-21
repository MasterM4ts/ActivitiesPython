#Programa que Altera o Custo Incluindo o Imposto Sobre o Custo.

def somaImposto(taxaImposto,custo):
    custo += taxaImposto
    return custo

print("+"+"="*40+"+")
custo = float(input("I| Digite o Custo do Item:\n>> "))
taxaImposto = float(input("I| Digite a Porcentagem de Imposto sobre as Vendas:\n>> "))
print("-"*38)
print("I| Valor Custo: R$%.2f"%custo)
print("I| Taxa do Imposto sobre o Custo: %.2f"%taxaImposto)
resultCusto = somaImposto(custo,taxaImposto)
print(f"I| Valor Com a Taxa de Imposto: R${resultCusto}")
print("-"*38)