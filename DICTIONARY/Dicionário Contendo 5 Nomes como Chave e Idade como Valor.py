#Dicionário Contendo 5 Nomes como Chave e Idade como Valor.

import os
for i in range(1,6):
    dicionario = {}
    print("-"*22)
    name = input("I| Digite o seu Nome:\n>> ")
    while True:
            try:
                idade = int(input("I| Digite sua Idade:\n>> "))
            except ValueError:
                print("\"Digite Somente Número Inteiro\"")
                os.system("pause")
                os.system("cls")
            else:
                
                break
    dicionario = {}
    os.system("pause")
    os.system("cls")