#Programa que Cadastra um Aluno e Calcula a Média das 4 Notas Bimestrais.

print("+"+"="*35+"+")
name = input("Digite seu Nome: \n>> ")
cidade = input("Digite sua Cidade: \n>> ")
escola = input("Digite sua Escola: \n>> ")
serie = input("Digite sua Série: \n>> ")
nota_1 = float(input("Digite a 1º Nota Bimestral: \n>> "))
nota_2 = float(input("Digite a 2º Nota Bimestral: \n>> "))
nota_3 = float(input("Digite a 3º Nota Bimestral: \n>> "))
nota_4 = float(input("Digite a 4º Nota Bimestral: \n>> "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

serie_1 = serie [:1]
serie_2 = serie [1:]

print("+"+"="*35+"+")
print(" "*10+"<Dados Coletados>")
print("+"+"="*35+"+")
print("I| Nome: %s."%name)
print("I| Cidade: %s."%cidade)
print("I| Escola: %s."%escola)
print("I| Série: %s º %s."%(serie_1,serie_2))
print("I| Média: %.2f"%media)
print("+"+"="*35+"+")