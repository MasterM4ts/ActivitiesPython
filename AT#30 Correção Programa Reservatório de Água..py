#Correção Programa Reservatório de Água. 

print("+"+"="*35+"+")
print(" "*6+"-- Resevartório de Água --")
print("+"+"="*35+"+")
altura = float(input("I| Digite a altura (cm): \n>> "))
largura = float(input("I| Digite a largura (cm): \n>> "))
comprimento = float(input("I| Digite o comprimento (cm): \n>> "))
c_diario = float(input("I| Digite o valor do consumo médio diário(litros/dia): \n>> "))
print("+"+"="*35+"+")

cap_total = ((altura*largura*comprimento)/1000) #O Resultado Seria em cm3 por isso, Dividimos por mil para Passar de cm3 para litros.
auton_reser = cap_total/c_diario

print("I| Capacidade do Reservatório: %.2f litros"%cap_total)
print("I| Autonomia do reservatório: %.2f dias"%auton_reser) 

#Agora, vamos Classificar o Consumo.

if(auton_reser < 2):
    print("+"+"="*35+"+")
    print("I| Consumo Elevado")
    print("+"+"="*35+"+")
elif(auton_reser >= 2 and auton_reser <= 7):
    print("+"+"="*35+"+")
    print("I| Consumo Moderado")
    print("+"+"="*35+"+")
else:
    print("+"+"="*35+"+")
    print("I| Consumo Baixo")
    print("+"+"="*35+"+")


#Programa com Erros.

'''print("-- Resevartório de Água --"

altura=float(input(" Digite a altura (cm):"))
largura=int(input(" Digite a largura (cm): ")
comprimento=float(input(" Digite o comprimento (cm): "))
c_diário float(input("Digite o valor do consumo médio diário(litros/dia)= "))

cap_total=((altura*largura,comprimento)/1000); o resultado seria em cm3 por isso, dividimos por mil para passar de cm3 para litros
auton_reser=cap_total/c_diario

print("Capacidade do Reservatório= ",cap_total, "litros ")
print("Autonomia do reservatório= ",auton_reser," dias") Agora, vamos classificar o consumo
if(auton_reser<2):
print("Consumo Elevado")
elif(auton_reser>=2 and auton_reser7):
     print("Consumo Moderado")
elif(auton_reser>7):
          	print("\n Consumo Baixo")'''