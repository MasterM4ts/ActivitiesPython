#Programa que Calcula a Média de Duas Notas.

print("+"+"="*35+"+")
nota_1 = float(input("I| Digite sua 1º Nota: \n>> "))
nota_2 = float(input("I| Digite sua 2º Nota: \n>> "))

media = (nota_1 + nota_2) / 2

if media >= 7.00:
    print("+"+"="*35+"+")
    print("I| Parabéns Aprovado!")
elif media >= 5.00 and 6.99:
    print("+"+"="*35+"+")
    print("I| Recuperação Estude Mais!")
else:
    print("+"+"="*35+"+")
    print("I| Que Triste Reprovado! Se Esforce Mais Ano que Vem")
    
print("I| Média: %.2f"%media)
print("+"+"="*35+"+")