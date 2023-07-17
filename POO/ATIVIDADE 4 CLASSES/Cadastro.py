import os
from pwinput import*
class Cadastro():


    def __init__(self,nome,cpf,telefone,email,endereco,senha):
        self.nome = nome
        self.__cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.__senha = senha

    
    def cadastro(self):
        nome = input("I| Digite seu Nome:\n>> ")
        cpf = input("I| Digite seu CPF:\n>> ")
        fone = input("I| Digite seu Telefone:\n>> ")
        email = input("I| Digite seu Email:\n>> ")
        endereco = input("I| Digite seu Endereço:\n>> ")
        senha = pwinput("I| Crie uma Senha:\n>> ")
        return nome,cpf,fone,email,endereco,senha