#Programa que Calcula a Quantia Total do seu Salário Naquele Mês. 

print("+"+"="*50+"+")
salario_Hora = float(input("Digite Quanto Ganha por Hora Trabalhada: \n>> "))
horas_Trabalho = float(input("Digite o Número de Horas Trabalhada: \n>> "))

salario_Total = salario_Hora * horas_Trabalho

print("+"+"="*30+"+")
print("I| Salario Total do Mês: R$%.4f"%salario_Total)
print("+"+"="*30+"+")