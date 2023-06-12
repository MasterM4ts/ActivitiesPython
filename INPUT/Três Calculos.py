#Programa 3 Calculos.

#O Produto do Dobro do Primeiro com Metade do Segundo.

print("+"+"="*30+"+")
num_1 = float(input("Digite um Número: \n>> "))
num_2 = float(input("Digite Outro Número: \n>> "))
num_3 = float(input("Digite um Terceio Número: \n>> "))

#O Produto do Dobro do Primeiro com Metade do Segundo.

result_1 = (num_1 * 2) * (num_2 / 2)

#A Soma do Triplo do Primeiro com Terceiro.

result_2 = (3 * num_2) + num_3

#O Terceiro Elevado ao Cubo.

result_3 = num_3**3


print("+"+"="*52+"+")
print(" "*21+"<Resultado>")
print("+"+"="*52+"+")
print("I| O Produto do Dobro do Primeiro com Metade do Segundo: \n>> %.2f"%result_1)
print("I| A Soma do Triplo do Primeiro com Terceiro: \n>> %.2f"%result_2)
print("I| O Terceiro Elevado ao Cubo: \n>> %.2f"%result_3)
print("+"+"="*52+"+")