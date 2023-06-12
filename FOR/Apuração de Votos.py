#Programa que Efetua a Apuração de Votos de Três Candidatos.

import os
print("+"+"="*35+"+")
eleitores = int(input("I| Digite Quantos Eleitores Votaram ? \n>> "))
cand_1 = 0
cand_2 = 0
cand_3 = 0
quant_votos = 0

for i in range(eleitores):
    votos = "x"
    while quant_votos != eleitores:
    
        print("+"+"="*35+"+")
        votos = input("I| Digite:\n1 >> Candidato 1\n2 >> Candidato 2\n3 >> Candidato 3\n>>")
        quant_votos +=1
        
        if votos == "1":
            cand_1 += 1
        elif votos == "2":
            cand_2 += 1
        elif votos == "3":
            cand_3 += 1
        else:
            print("I| \"Erro\" Tente Novamente.")
        
os.system("cls")
print("+"+"="*30+"+")
print("I| Votos Efetuados \"%d\""%quant_votos)
print("-"*18)
print("I| Candidato 1: %d"%cand_1)
print("I| Candidato 2: %d"%cand_2)
print("I| Candidato 3: %d"%cand_3)
print("+"+"="*30+"+")