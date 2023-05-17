#Programa que Calcula a Área de um Quadrado e Imprime o Dobro da Área.

print("+"+"="*30+"+")
lado_Quadrado = float(input("Digite um Lado do Quadrado: \n>> "))

area = lado_Quadrado**2
dobro_Area = area*2

print("+"+"="*35+"+")
print(" "*13+"<Resultado>")
print("+"+"="*35+"+")
print("I| Área do Quadrado: %.2f"%area)
print("I| Dobro da Área do Quadrado: %.2f"%dobro_Area)
print("+"+"="*35+"+")

