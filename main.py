import env
from modules.mySql import createTable, readTable, readColumnsTable

## Definindo path do arquivo csv kaggle
path_csv = env.PATH_CSV

def main():
    ## Criando a tabela movies
    columns_remove = ['Rate', 'Metascore']
    createTable(path_csv, columns_remove, 'MOVIES')
    
    ## Criando a tabela ratings
    columns_remove = ['Original Title',
                  'Company',
                  'Release',
                  'Minutes',
                  'Budget',
                  'Opening Weekend USA',
                  'Gross USA',
                  'Gross Worldwide']
    createTable(path_csv, columns_remove, 'RATINGS')

    movies = readTable('MOVIES')
    # print(movies)
    ratings = readTable('RATINGS')
    # print(ratings)    
    columns_movies = readColumnsTable('MOVIES')
    # print(columns_movies)
    columns_ratings = readColumnsTable('RATINGS')

main()