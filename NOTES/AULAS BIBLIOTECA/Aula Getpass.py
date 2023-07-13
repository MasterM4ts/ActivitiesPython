#Apresentação#

from getpass import getpass

senha = getpass("Digite Sua Senha: ")
confirmar_senha = getpass("Confirme sua Senha: ")

if senha == confirmar_senha:
    print("I| Senha \"Correta!\"")
else:
    print("I| \"Senha Incorreta\"")