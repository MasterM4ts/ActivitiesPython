import mysql.connector

con = mysql.connector.connect(
    host= '10.28.1.195',
    database = 'HUB_INNOVATION',
    user = 'suporte',
    password = 'suporte'
)

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao Banco de Dados =',db_info)
    
    
consulta_sql = 'SELECT * FROM USUARIO'
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print('Número Total de Registros Retornados: ',cursor.rowcount)


print('Mostrar os Registros')
for linha in linhas:
    print('ID_USUARIO: ',linha[0])
    print('NOME : ', linha[1])
    print('E-MAIL: ', linha[2])
    print('TELEFONE: ', linha[3])
    print('CPF: ', linha[4])
    print('DATA DE NASCIMENTO: ', linha[5])
    print('GENERO: ', linha[6])
    print('OPCAO_1: ', linha[7])
    print('OPCAO_2: ', linha[8])
    print('='*35)

# INSERT  
# comando = """INSERT INTO USUARIO (ID_USER, NOME, E_MAIL, TELEFONE, CPF, DATA_NASCIMENTO, GENERO, OPCAO_1, OPCAO_2) VALUES 
# (NULL, 'Galileu', 'galileujesus@gmail.com', '(67) 99957-6598', '003.687.679-55', '2000-12-25', 1, 1, 1);"""
# cursor.execute(comando)
# con.commit()

# UPDATE
# comando = """UPDATE USUARIO SET NOME = 'Espirito Santo' WHERE CPF = '003.687.679-55';"""
# cursor.execute(comando)
# con.commit()

# DELETE
# comando = """DELETE FROM USUARIO WHERE CPF = '003.687.679-55';"""
# cursor.execute(comando)
# con.commit()


if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão Encerrada")