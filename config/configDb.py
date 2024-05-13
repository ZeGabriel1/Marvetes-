import mysql.connector
import env

def connectDb():
    try:
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database=env.DATABASE
    )

        if db.is_connected():
            print('Banco de dados MySQL conectado com sucesso!')
        
        return db

    except Exception as e:
        print(f'Ocorreu um erro na conexao com o banco de dados MySQL: {e}')