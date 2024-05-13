# Marvetes

> Sistema de leitura e normalização de documento CSV para MYSQL e do MYSQL para MONGODB

### Roadmap do Projeto

- [x] Configurar ambiente de desenvolvimento e virtual
- [x] Configurar documeto do docker-compose
- [x] Ler CSV
- [x] Verificar se o DataFrame precisa de tratamento de tipo
- [x] Elaborar modelo lógico dos dados
- [x] Enviar dados para suas respectivas tabelas no MYSQL
- [x] Criar conexão com o banco de dados MYSQL
- [x] Ler as tabelas no MYSQL
- [x] Normalizar dados para NOSQL/MONGODB
- [x] Criar conexão com o banco de dados MYSQL e configurar coleção
- [x] Enviar os dados para a coleção no MONGODB

## Pré-requisitos

- `Ter o Docker instalado`
- `Ter o Python 3+ instalado`

## Instalando o projeto

1 - Clonar o projeto do repositorio no github
```
git clone https://github.com/ZeGabriel1/Marvetes-.git
```

2 - Acessar a pasta local do projeto
```
cd pasta_do_projeto
```

3 - Criar um ambiente virtual

```
python -m venv venv
```


4 - Inicie o docker compose com o comando

```
docker-compose up -d
```

5 - Inicie o ambiente virtual no powershell

```
.\venv\Script\active.ps1
```

6 - Instale as dependências

```
pip install -r requirements.txt
```

7 - Inicie a aplicação de injeção de dados no MySQL e MONGODB

```
py main.py
```


## Comandos Docker

- verificar quais imagens

```
docker images 
```

- verificar quais containers estão rodando

```
docker ps 
```

- Parar os containers

```
docker-compose stop
```

- Ou para parar apenas um container 

```
docker stop {container}
```


## Comandos MySQL
1 - Acessa a máquina que está rodando o container mysql

```
docker exec -it mysql //bin//sh
```

2 - Acessa o mysql

```
mysql -u root -p -A
```
depois precisa passar a senha "root"

3 - Para selecionar o banco

```
USE {database}
```

4 - Para Exibir os bancos de dados

```
SHOW DATABASES;
```

5 - Para exibir as colunas de um banco de dados

```
show tables FROM {database};
```

6 - Para exibir os dados de uma tabela

1º Selecione a tabela

```
USE {database}
```

2º Consulte a tabela

```
SELECT * FROM movies;
```


## Comandos MongoDB

- 1º Para acessar o container do mongo
```
docker exec -it mysql //bin//sh
```

- 2º Para acessar o terminal do mongo
```
mongosh
```

- 3º Navegar para o user admin para se autenticar
```
use admin
```

- 4º Para autenticar no mongodb digite
```
db.auth('root', passwordPrompt())
```
Em seguida coloque a senha

- 5º Para mostrar os bancos de dados digite
```
show dbs
```

- Para criar um db digite
```
use nome_do_db
```

- Para criar uma coleção digite
```
db.createCollection("nome_da_coleção")
```