#Programa que Calcula o Valor do Novo Sálario reajustado de Acordo com a Tabela Abaixo:

'''  Salário Atual        |       Reajuste
==========================|=====================                         
    Abaixo de R$500,00    |          15%
de R$500,00 até R$1000,00 |          10%
    acima de R$1000,00    |           5%
==========================|====================='''

print("+"+"="*35+"+")
salario_Anterior = float(input("I| Digite seu Salário Atual: \n>> "))


if salario_Anterior < 500.00:
    reajuste = salario_Anterior / 15/100
    salario_Atual = salario_Anterior + reajuste
    
    print("+"+"="*35+"+")
    print("I| Seu Salário teve um Reajuste de 15%.")
    print("I| Salário Anterior: %.2f"%salario_Anterior)
    print("I| Salário ATual: %.2f"%salario_Atual)
    print("I| Valor do Reajuste: %.2f"%reajuste)
    print("+"+"="*35+"+")


elif salario_Anterior == 500.00 and salario_Anterior <= 1000.00:
    reajuste = salario_Anterior /  10/100
    salario_Atual = salario_Anterior + reajuste
    
    print("+"+"="*35+"+")
    print("I| Seu Salário teve um Reajuste de 10%.")
    print("I| Salário Anterior: %.2f"%salario_Anterior)
    print("I| Salário ATual: %.2f"%salario_Atual)
    print("I| Valor do Reajuste: %.2f"%reajuste)
    print("+"+"="*35+"+")


else:
    reajuste = salario_Anterior / 5/100
    salario_Atual = salario_Anterior + reajuste
    
    print("+"+"="*35+"+")
    print("I| Seu Salário teve um Reajuste de 5%.")
    print("I| Salário Anterior: %.2f"%salario_Anterior)
    print("I| Salário ATual: %.2f"%salario_Atual)
    print("I| Valor do Reajuste: %.2f"%reajuste)
    print("+"+"="*35+"+")