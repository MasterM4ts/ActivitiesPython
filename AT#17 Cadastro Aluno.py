#Programa que Cadastra um Aluno e Calcula a Média das 4 Notas Bimestrais.
print("+"+"="*35+"+")
name = input("Digite seu Nome: \n>> ")
cidade = input("Digite sua Cidade: \n>> ")
escola = input("Digite sua Escola: \n>> ")
serie = input("Digite sua Série: \n>> ")
nota_Um = float(input("Digite a 1º Nota Bimestral: \n>> "))
nota_Dois = float(input("Digite a 2º Nota Bimestral: \n>> "))
nota_Tres = float(input("Digite a 3º Nota Bimestral: \n>> "))
nota_Quatro = float(input("Digite a 4º Nota Bimestral: \n>> "))

media = (nota_Um + nota_Dois + nota_Tres + nota_Quatro) / 4

serie_Um = serie [:1]
serie_Dois = serie [1:]

print("+"+"="*35+"+")
print(" "*10+"<Dados Coletados>")
print("+"+"="*35+"+")
print("I| Nome: %s."%name)
print("I| Cidade: %s."%cidade)
print("I| Escola: %s."%escola)
print("I| Série: %s º %s."%(serie_Um,serie_Dois))
print("I| Média: %.2f"%media)
print("+"+"="*35+"+")