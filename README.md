# Desafio-BackEnd

Para inciar este projeto, é necessário instalar as dependências, que serão utilizadas no projeto. Portanto utilize o comando abaixo para instalar tais dependências:

```
pip install -r requirements.txt
```

Para registrar as migrações no banco de dados:

```
python manage.py migrate
```

Para iniciar a aplicação:

```
python manage.py runserver
```

Os arquivos são salvos na pasta /tmp na raiz do projeto.

Para fazer o upload das transações, acesse:

```
http://127.0.0.1:8000/upload


```
Para visualizar as transações, acesse:

```
http://127.0.0.1:8000/lista
```