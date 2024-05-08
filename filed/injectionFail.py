## Importando biblioteca e modulo
import pandas as pd
from config import configDb

## Definindo path do arquivo csv kaggle
path_csv = '.\data\db.csv'

## Armazendando o csv em um dataframe
df = pd.read_csv(path_csv, encoding='unicode_escape')

## Consultando/verificando o dataframe
# print(df.head())
# print(df.info())

## Excluindo primeira coluna unnamed
df = df.drop(columns='Unnamed: 0',axis=0)

## Inicializando conexão com o mysql
db = configDb.connectDb()

## Inicializando cursor que trabalha com o SQL
cursor = db.cursor()

## Lendo todas as linhdas do csv
for indice, row in df.iterrows():
    # print(row['Original Title'])
    
    values = []
    
    for data in row:
        data = str(data).replace(' ', '')
        values.append(data)
        
    # print(values)
    
    values_Tuple = tuple(values)
    
    # print(values_Tuple)
    
    ## Script SQL de inserção
    # sql = """INSERT INTO filmes (original_title, company, rate, metascore, minutes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    ## Executando o script e passando os valores
    # cursor.execute(sql, values_Tuple)

## Confirmando a inserção de dados    
db.commit()
print("Dados inseridos com sucesso!")

## Finalizando cursor e conexão com o mysql
cursor.close()
# db.close()