#Programa que Imprime Bom Dia,Boa Noite,Boa Tarde ou Valor Invalido de Acordo com o Turno que o Usúario Digitar.

print("+"+"="*35+"+")
turno = input("I| Digite o Turno que Estuda: \nI| M = Matutino \nI| V = Vespertino \nI| N = Noturno \n>> ")

turno = turno.upper()

if turno == "M":
    print("+"+"="*20+"+")
    print("Bom Dia")
    print("I| Turno: %s = Matutino"%turno)
    print("+"+"="*20+"+")

elif turno == "V":
    print("+"+"="*20+"+")
    print("Boa Tarde")
    print("I| Turno: %s = Vespertino"%turno)
    print("+"+"="*20+"+")

elif turno == "N":
    print("+"+"="*20+"+")
    print("Boa Noite")
    print("I| Turno: %s = Noturno"%turno)
    print("+"+"="*20+"+")

else:
    print("+"+"="*20+"+")
    print("Turno Inválido")
    print("+"+"="*20+"+")