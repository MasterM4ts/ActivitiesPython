import mysql.connector

con = mysql.connector.connect(
    host= '10.28.1.195',
    database = 'CADASTRO',
    user = 'suporte',
    password = 'suporte'
)

cursor = con.cursor()



if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão Encerrada")