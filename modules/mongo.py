import pymongo

# Criando um cliente para o serviço do MongoDB rodando localmente na porta 27017
mongodb_client = pymongo.MongoClient('mongodb://root:example@localhost:27017/')

# Selecionanndo uma base de dados chamada 'students'
database = mongodb_client['marvelvsdc']

# Selecionando uma coleção chamada 'students'
collection = database['movies']

def createDoc(doc):
    try:
        result = collection.insert_one(doc)
        if result.acknowledged:
            print('Documento inserido com sucesso')
        else:
            print('Falha ao inserir o documento')
    except Exception as e:
        print(f'Um erro ocorreu: {e}')