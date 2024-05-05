import mysql.connector

def connectDb():

    db = mysql.connector.connect(
        host="localhost",
        user="user",
        password="user",
        database="marvel"
    )

    if db.is_connected():
        print('Banco de dados conectado com sucesso!')
    
    return db