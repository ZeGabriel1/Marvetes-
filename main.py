import env
from modules.mySql import createTable, readTable, readColumnsTable
from modules.mongo import createDoc


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

     ## Normalizando as tableas SQL para docs NOSQL
    for indiceMovie, movie in enumerate(movies):
        doc = {}
        for indice, column in enumerate(columns_movies):
            # print(column[0], movie[indice])
            if indice != 0:
                doc[column[0]] = movie[indice]
        
        for indiceRate, rate in enumerate(ratings):   
            doc_rate = {}       
            # print(rate)
            if indiceMovie == indiceRate:
                for indice, column in enumerate(columns_ratings):                
                    if indice != 0:         
                        # print(indice, column)           
                        doc_rate[column[0]] = rate[indice]
                # print(doc_rate)            
                doc['Ratings'] = doc_rate
                
        # print(doc)
        createDoc(doc)

main()