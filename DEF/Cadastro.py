#Programa que Efetua um Cadastro e Informa seu Nome e Idade Utilizando uma Função.

def cadastro():
    name = input("I| Digite seu Nome:\n>> ")
    age = int(input("I| Digite sua Idade:\n>> "))
    return name,age

print("I| Iniciando Cadastro...")
name,idade = cadastro()
print("I| Cadastro Realizado com Sucesso.")
print("I|Seu Nome é %s e você tem %d anos de Idade."%(name,idade))
print("="*50)