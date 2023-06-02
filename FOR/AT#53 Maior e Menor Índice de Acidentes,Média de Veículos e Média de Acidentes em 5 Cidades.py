#Programa que Informa o Maior e Menor Índice de Acidentes,Média de Veículos e Média de Acidentes em 5 Cidades.

maior = -1
menor = 9999999999
soma_V = 0
soma_A2000 = 0
cont = 0
for i in range(5):
    quant_veiculos = int(input("I| Digite a Quantidade de Veículos:\n>> "))
    quant_acidentes = int(input("I| Digite a Quantidade de Acidentes:\n>> "))
    
    if quant_acidentes > maior:
        maior = quant_acidentes
        cidade_maior = i + 1

    if quant_acidentes < menor:
        menor = quant_acidentes
        cidade_menor = i + 1

    soma_V += quant_veiculos
    
    if quant_acidentes < 2000:
        soma_A2000 + quant_acidentes
        cont += 1

media = soma_V / 5
media2000 = soma_V / cont

print("+"+"="*35+"+")
print("I| Maior e Menor Índice %d e %d, Cidades que Pertence: %d e %d"%(maior,menor,cidade_maior,cidade_menor))
print("I| Média de Veiculos nas 5 Cidades: %d"%media)
print("I| Media de Acidentes nas Cidades com Menos de 2000 Veículos: %d"%media2000)
print("+"+"="*35+"+")