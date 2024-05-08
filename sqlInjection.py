## Importando biblioteca e modulo
import pandas as pd
from config import configDb
from sqlalchemy import create_engine

## Definindo path do arquivo csv kaggle
path_csv = '.\data\db.csv'

## Armazendando o csv em um dataframe
df = pd.read_csv(path_csv, encoding='unicode_escape')

## Consultando/verificando o dataframe
# print(df.head())
# print(df.info())

## Excluindo primeira coluna unnamed
df = df.drop(columns='Unnamed: 0',axis=0)

## Configurando parametro de conexão com o Banco de dados
params = "mysql+mysqlconnector://root:root@localhost/marvel"

## 
engine = create_engine(params, echo=True)

## Enviando os dados para o bando de dados MYSQL
df.to_sql('movies', con=engine, if_exists='append', index=False)