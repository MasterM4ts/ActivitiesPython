#Programa que Calcula a Multa sobre as Prestações.
 
import os
def valorPagamento(valor,diasAtraso):
    if diasAtraso > 0:
        multa = (valor * 3/100) + valor
        juros = diasAtraso * (valor * 0.1/100)
        result = multa + juros
        print("I| Valor a ser Pago: %.2f"%result)
        relatorio.append(valor)
    else:
        print("I| Valor a ser Pago: %.2f"%result)
        relatorio.append(valor)
inicio = 1
relatorio = []
while inicio != 0:
    print("="*34)
    inicio = int(input("I| DIGITE:\n1 >> Iniciar Calculo de Prestação.\n0 >> Relatório(Encerrar Programa)\n>> "))
    if inicio == 1:
        valor = float(input("I| Digite o Valor da Prestação:\n>> "))
        diasAtraso = int(input("I| Digite os Dias em Atraso:\n>> "))
        print("-"*20)
        valorPagamento(valor,diasAtraso)
        print("-"*20)
        os.system("pause")
        os.system("cls")

    else:
        print("I| Relatório:")
        for i in relatorio:
            print("I| %s"%i)
        print("I| Valor Total do Relatório: R$",sum(relatorio))
        break