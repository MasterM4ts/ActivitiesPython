#Programa que Completa um Dicionario com uma Chave para Cada Dia da Semana.
#Tendo como seu Valor as Aulas que você tem Nesse Dia.

final_semana = []
aulas = [[5],[5],[6],[4],[2]]
dicionario = {"Domingo":final_semana,"Segunda":aulas[0],"Terça":aulas[1],"Quarta":aulas[2],"Quinta":aulas[3],"Sexta":aulas[4],"Sábado":final_semana}
print("I| Domingo:",dicionario ["Domingo"])
print("I| Segunda:",dicionario ["Segunda"])
print("I| Terça:",dicionario ["Terça"])
print("I| Quarta:",dicionario ["Quarta"])
print("I| Quinta:",dicionario ["Quinta"])
print("I| Sexta:",dicionario ["Sexta"])
print("I| Sábado:",dicionario ["Sábado"])