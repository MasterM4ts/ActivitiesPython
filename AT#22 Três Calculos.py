#Programa 3 Calculos.

#O Produto do Dobro do Primeiro com Metade do Segundo.

print("+"+"="*30+"+")
num_Um = float(input("Digite um Número: \n>> "))
num_Dois = float(input("Digite Outro Número: \n>> "))
num_Tres = float(input("Digite um Terceio Número: \n>> "))

#O Produto do Dobro do Primeiro com Metade do Segundo.

result_Um = (num_Um * 2) * (num_Dois / 2)

#A Soma do Triplo do Primeiro com Terceiro.

result_Dois = (3 * num_Um) + num_Tres

#O Terceiro Elevado ao Cubo.

result_Tres = num_Tres**3


print("+"+"="*52+"+")
print(" "*21+"<Resultado>")
print("+"+"="*52+"+")
print("I| O Produto do Dobro do Primeiro com Metade do Segundo: \n>> %.2f"%result_Um)
print("I| A Soma do Triplo do Primeiro com Terceiro: \n>> %.2f"%result_Dois)
print("I| O Terceiro Elevado ao Cubo: \n>> %.2f"%result_Tres)
print("+"+"="*52+"+")