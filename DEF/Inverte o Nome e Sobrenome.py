#Programa que Inverte o Nome e Sobrenome Digitados pelo Usuário.

def inverte(name,sobname):
    nameInverso = sobname + "," + name
    return nameInverso
name = input("I| Digite seu Nome:\n>> ")
sobname = input("I| Digite seu Sobre Nome:\n>> ")
invertido = inverte(name,sobname)
print("Olá",invertido)