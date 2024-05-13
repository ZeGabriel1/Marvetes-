## Importando biblioteca e modulo
import pandas as pd
from sqlalchemy import create_engine
import env
from config.configDb import connectDb

## Configurando parametro de conexão com o Banco de dados
params = env.CONFIG_CONNECTION_MYSQL

## Criando engine
engine = create_engine(params, echo=True)

## Conexão com db MySQL
db = connectDb()


## Armazendando o csv em um dataframe
def readCsv(path):
    df = pd.read_csv(path, encoding='unicode_escape')
    return df


def createTable(path, cols_remove, table):
    try:
        df = readCsv(path)

        ## Renomeando a coluna vázia para Id
        df = df.rename(columns={'Unnamed: 0': 'Id'})

        ## Excluindo primeira coluna unnamed
        # df = df.drop(columns='Unnamed: 0',axis=0)
        
        colums_remove = cols_remove
        df = df.drop(columns=colums_remove)
        
        ## Consultando/verificando o dataframe
        print(df.head())
        print(df.info())
        
        ## Enviando os dados para o bando de dados MYSQL
        df.to_sql(table, con=engine, if_exists='append', index=False)
        print(f'Tabela {table} criada com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro na criação da tabela {table}: {e}')


def readColumnsTable(table):
    try:
        ## Inicializando o cursor
        cursor = db.cursor()
        
        ## Armazenando o comando de consulta no MySQL
        comand = f'DESCRIBE {table}'
        
        ## Executa o cursor
        cursor.execute(comand)        
        
        ## Pegando o resultado
        result = cursor.fetchall()        
        # print(result)
        
        ## Fecha o cursor
        cursor.close()        
        print(f'Colunas da tabela {table} lidas com sucesso!')
        return result 
    
    except Exception as e:
        print(f'Erro ao ler as colunas da tabela: {e}')


def readTable(table):
    try:        
        ## Inicializando o cursor
        cursor = db.cursor()
        
        ## Armazenando o comando de consulta no MySQL
        comand = f'SELECT * FROM {table}'
        
        ## Executa o cursor
        cursor.execute(comand)        
        
        ## Pegando o resultado
        result = cursor.fetchall()        
        # print(result)
        
        ## Fecha o cursor
        cursor.close()        
        print('Tabela lida com sucesso!')
        return result
    
    except Exception as e:
        print(f'Erro ao tentar ler a tabela MySQL: {e}')