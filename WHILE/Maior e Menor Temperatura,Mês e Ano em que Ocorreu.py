#Programa que Lê um Conjunto de Temperatura bem Como o Mês e Ano que Ocorreu.
#Informa a Maior e Menor Temperatura Informadas, o Mês e Ano em que Ocorreu.
#Fazendo a Média das Temperaturas Digitadas Pelo Usúario.

temperaturas = []
meses = []
anos = []
cont = 1
while True:
    print("+"+"="*35+"+")
    temperatura = float(input("I| Digite a Temperatura:\n>> "))
    while True:
        mes = int(input("I| Digite o Mês que Ocorreu a Temperatura:\n>> "))
        if mes < 1 and mes > 12:
            print("I| Mês Invalido!")
        else:
            break
    ano = input("I| Digite Ano que Ocorreu a Temperatura:\n>> ")

    temperaturas.append(temperatura)
    meses.append(mes)
    anos.append(ano)
    maior = max(temperaturas)
    menor = min(temperaturas)
    indice_maior = temperaturas.index(maior)
    indice_menor = temperaturas.index(menor)
    media = sum(temperaturas) / cont
    
    print("+"+"="*35+"+")
    inicio = int(input("I| Digite: \nI| 1 >> Continuar. \nI| 0 >> Resultados.\n>> "))
    print("-"*37)
    if inicio == 0:
        print("+"+"="*35+"+")
        print("I| Maior e Menor Temperatura: %.2f e %.2f"%(maior,menor))
        print("I| Mês da Maior e Menor Temperatura: %d e %d"%(meses[indice_maior],meses[indice_menor]))
        print("I| Ano da Maior e Menor Temperatura: %s e %s"%(anos[indice_maior],anos[indice_menor]))
        print("I| Média de Todas as Temperaturas: %.2f"%media)
        print("-"*37)
        break
    else:
        cont += 1
        continue