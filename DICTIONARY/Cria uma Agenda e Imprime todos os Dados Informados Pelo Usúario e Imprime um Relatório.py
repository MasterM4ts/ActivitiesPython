#Programa que Cria uma Agenda e Imprime todos os Dados Informados Pelo Usúario e Imprime um Relatório.

import os
dicionario_agenda = ["Domindo","Sugunda","Terça","Quarta","Quinta","Sexta","Sabádo"]
dicionario = {}
inicio = 1
cont = 0
while True:
    print("="*53)
    print("I| \"Agenda de Domingo a Sabádo\"")
    print("I| Domindo\\Sugunda\\Terça\\Quarta\\Quinta\\Sexta\\Sabádo")
    print("I| OBS: Digite 0 para Relatório(Encerrar o Programa)")
    inicio = int(input("I| Digite:\n1 >> Iniciar\n0 >> Relatório\n>> "))
    if inicio == 1:
        cont += 0
        cpf = input("I| Digite seu CPF:\n>> ")
        name = input("I| Digite seu Nome:\n>> ")
        idade = int(input("I| Digite sua Idade:\n>> "))
        fone = int(input("I| Digite seu Telefone:\n>> "))
        dicionario[cpf] = name,idade,fone
        print("\""+dicionario_agenda[cont]+"\"",dicionario)
        os.system("pause")
        os.system("cls")
    elif inicio == 0:
        cpf = input("I| Digite Qual Relatório Deseja Analizar:\n>> ")
        print("I| ",dicionario[cpf])
        print()
        print("-"*22)
        print("I| Programa Encerrado")
        print("-"*22)
        break