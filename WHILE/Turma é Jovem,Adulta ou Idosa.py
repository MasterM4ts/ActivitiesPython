#Programa que Pede a Idade de X Pessoas e Informa se se a Média da Turma é Jovem,Adulta ou Idosa.

import os
idades = []
cont = 0
while True:
    print("+"+"="*35+"+")
    print("I| OBS: Digite 0 Para Sair.")
    print("+"+"="*35+"+")
    idade = int(input("I| Digite sua Idade:\n>>"))
    print("+"+"="*35+"+")
    cont += 1
    os.system("cls")
    
    if idade == 0:
        break

    
    idades.append(idade)
    

media = sum(idades) / cont

if media > 0 and media <= 25:
    print("+"+"="*35+"+")
    print("I| A Média da Turma é %d "%media)
    print("I| Turma \"Jovem\"") 

elif media >= 26 and media <= 60:
    print("+"+"="*35+"+")
    print("I| A Média da Turma é %d "%media)
    print("I| Turma \"Adulta\"") 
    

else:
    print("+"+"="*35+"+")
    print("I| A Média da Turma é %d "%media)
    print("I| Turma \"Idosa\"") 
    

print("+"+"="*35+"+")
print("I| Programa Encerrado.")
print("+"+"="*35+"+")