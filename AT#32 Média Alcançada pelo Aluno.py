#Programa que Calcula a Média Alcançada pelo Aluno.

print("+"+"="*35+"+")
nota_1 = float(input("I| DIgite sua 1º Nota: \n>> "))
nota_2 = float(input("I| Digite sua 2º Nota: \n>> "))

media = (nota_1 + nota_2) / 2

if media >= 7.00:
    print("+"+"="*35+"+")
    print("I| Aprovado!")
    print("+"+"="*35+"+")
    if media == 10.00:
        print("+"+"="*35+"+")
        print("I| Distinção!")
        print("+"+"="*35+"+")
else:
    print("+"+"="*35+"+")
    print("I| Reprovado!")
    print("+"+"="*35+"+")