import mysql.connector
import os

con = mysql.connector.connect(
    host= '10.28.1.195',
    database = 'CADASTRO',
    user = 'suporte',
    password = 'suporte'
)
if con.is_connected():
    db_info = con.get_server_info()
    print('#' + '='*17 + '#')
    print('Conectado ao Banco de Dados =',db_info)
    print('#' + '='*17 + '#')


cursor = con.cursor()

while True:
    print('#' + '='*17 + '#')
    print("Cadastro de Cliente")
    print('#' + '='*17 + '#')
    
    while True:
        try:
            name = input("I| Digite seu Nome: \n>> ")
            sob_name = input("I| Digite seu Sobrenome: \n>> ")  
            idade = int(input("I| Digite sua Idade: \n>> ")) 
            rg = input("I| Digite seu RG: \n>> ") 
            cpf = input("I| Digite seu CPF: \n>> ") 
            estado = input("I| Digite seu Estado: \n>> ") 
            cid = input("I| Digite sua Cidade: \n>> ")
            endereco = input("I| Digite seu Endereço: \n>> ")
            fone = (input("I| Digite seu Telefone: \n>> "))
            email = input("I| Digite seu Email: \n>> ")
            print('#' + '='*17 + '#')
            os.system("pause")
            os.system("cls")
        
        except ValueError:
            print('#' + '='*17 + '#')
            print("Preenchimente de Campo Invalido\nTente Novamente")
            print('#' + '='*17 + '#')
            
        else:
            comando = f"""INSERT INTO CLIENTE (ID, NOME, SOB_NOME, IDADE, RG, CPF, ESTADO, CIDADE, ENDERECO, TELEFONE, EMAIL) VALUES 
            (NULL, '{name}', '{sob_name}', {idade}, '{rg}', '{cpf}', '{estado}', '{cid}', '{endereco}', '{fone}', '{email}');"""
            cursor.execute(comando)
            con.commit()
            print('#' + '='*17 + '#')
            print('Cadastro Efetuado com Sucesso')
            print('#' + '='*17 + '#')
            os.system("pause")
            os.system("cls")
            break
    
    break
     
            
if con.is_connected():
    cursor.close()
    con.close()
    print('#' + '='*17 + '#')
    print("Conexão Encerrada")
    print('#' + '='*17 + '#')