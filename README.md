# Marvetes

1 - Criar um ambiente virtual

```
python -m venv venv
```


2 - Inicie o docker compose com o comando

```
docker-compose up -d
```

3 - Inicie o ambiente virtual no powershell

```
.\venv\Script\active.ps1
```

4 - Instale as deendências

```
pip install -r requirements.txt
```

5 - Inicie a aplicação de injeção de dados no MySQL

```
py sqlInjection.py
```


## Comandos úteis

- verificar quais imagens

```
docker images 
```

- verificar quais containers estão rodando

```
docker ps 
```

- Acessa a marquina que está rodando o container

```
docker exec -it mysql //bin//sh
```

- Acessa o mysql

```
mysql -u user -p -A
```
depois precisa passar a senha "user"

- Para selecionar o banco

```
USE marvel
```

- Para Exibir os bancos de dados

```
SHOW DATABASES;
```

- Para exibir as colunas de um banco de dados

```
show tables FROM 'database';
```

- Para exibir os dados de uma tabela

1º Selecione a tabela

```
USE marvel
```

2º Consulte a tabela

```
SELECT * FROM movies;
```
