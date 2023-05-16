###################################################     //1//

#Programa que Permite Somente Nota de 0 até 10.

print("+"+"="*35+"+")
nota = float(input("I| Digite uma Nota de 0 até 10: \n>> "))
while (nota < 0) or (nota > 10):
    nota = float(input("I| Não pode ser menor qoe 0 ou maior que 10: \nTemte Novamente: \n>> "))
print("I| Nota Válida.")

###################################################     //2//   

#Programa que não Permite Nome e Senha Iguais.

print("+"+"="*35+"+")
nome = input("I| Digite seu Nome: \n>> ")
senha = input("I| Digite seu Nome: \n>> ")

while nome == senha:
    print("="*24)
    print("Erro | Tente Novamente.")
    print("="*24)
    nome = input("I| Digite seu Nome: \n>> ")
    senha = input("I| Digite seu Nome: \n>> ")
print("+"+"="*35+"+")
print("I| Acesso Consedido.")
print("+"+"="*35+"+")

###################################################     //3// 

#Programa que Recebe Informações do Usúario.

print("+"+"="*35+"+")
nome = input("I| Digite seu Nome: \n>> ")
idade = input("I| Digite sua Idade: \n>> ")
salario = float(input("I| Digite seu Salário: \n>> "))
sexo = input("I| Digite seu Sexo: \nI| M \nI| F>> ")
civil = input("I| Digite seu Estado Civil: \nI| S \nI| C \nI| V \nI| D \n>> ")

sexo = sexo.upper
civil = civil.upper

while len(nome) <= 3:
    print("+"+"="*35+"+")
    nome = input("I| Seu Nome Deve Conter Mais de 3 Caracteres: \n>> ")

while (idade < 0) or (idade > 150):
    print("+"+"="*35+"+")
    idade = input("I| Você Deve ter Entre 0 e 150 Anos: \n>> ")

while (salario < 0):
    print("+"+"="*35+"+")
    salario = input("I| A Coisa tá Difícil, mas não Existe Salário Negativo: \n>> ")

while (sexo != "F") and (sexo != "M"):
    print("+"+"="*35+"+")
    sexo = input("I| Você Deve ser Biologicamente 'F' ou 'M': \n>> ")

while (civil != "S") and (civil != "C") and (civil != "V") and (civil != "D"):
    print("+"+"="*35+"+")
    civil = input("I| Deve ser S,C,V ou D: \n>> ")

print("+"+"="*35+"+")
print("I| Concluido.")
print("+"+"="*35+"+")

###################################################     //4//

#Programa que Calcula a Taxa de Crecimento do País A e B.
#O Calculo é Efetuado até a População do País A Ultrapassar a População do País B.

print("+"+"="*35+"+")
ano = 0
a = 80000
b = 200000

while a < b:
    a = 80000 + 3/100
    b = 200000 + 1.5/100
    ano += 1

print("I| Demorou %d Para a Populacão de A Ultrapassar a População B."%ano)

###################################################     //5//

#Programa que Calcula a Taxa de Crecimento do País A e B.
#O Calculo é Efetuado até a População do País A Ultrapassar a População do País B.

print("+"+"="*35+"+")
a = int(input("I| Qual a População do País A: \n>> "))
while a < 0:
    a = int(input("I| A População do País A Deve ser Maior que 0: \n>> "))
taxa_A = float(input("I| Qual a Taxa de Crecimento do País A: \n>> "))

b = int(input("I| Qual a População do País B: \n>> "))
while b < 0:
    b = int(input("I| A População do País B Deve ser Maior que 0: \n>> "))
taxa_B = float(input("I| Qual a Taxa de Crecimento do País B: \n>> "))

ano = 0
while a < b:
    ano += 1
    a = int((1 + (taxa_A/100)) * a)
    b = int((1 + (taxa_B/100)) * b)
    print("I| Anos>: %d"%ano)
    print("I| População A: %d"%a)
    print("I| População B: %d"%b)

print("Ultrapassa no Ano: %d"%ano)

###################################################     //6//   