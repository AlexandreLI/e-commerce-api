# e-commerce-api
Backend Api do E-Commerce

# Dependências
Python 3.12.3 ou superior\
Poetry 1.8.2\
Make (Opcional)

# Instalação

1 - Na raiz do projeto, instale as dependecias do python com o seguinte comando:

```
poetry install
```

2 - Ative o ambiente virtual do poetry:
```
poetry shell
```

3 - Execute as migrações do banco de dados
```
python manage.py migrate
```
ou usando o make
```
make migrate
```

4 - Insira os dados iniciais no banco de dados com o comando abaixo:
```
python manage.py loaddata src/django_project/fixtures/initial_data.json
```
ou com o make
```
make fixtures
```

5 - Rode a aplicação em modo de desenvolvimento
```
python manage.py runserver
```
ou com o make
```
make run
```

# Testes
Para rodas os testes unitarios e de integração execute o comando abaixo:

```
python -m pytest
```
ou com o make
```
make test
```

Para saber a cobertura de testes execute o comando abaixo:

```
python -m pytest -v --cov-report term-missing --cov=src/ --cov-report=html --cov-config=.coveragerc
```
ou com o make
```
make coverage
```

Para testar a API via Postman acesse a pasta postman_collection e import o arquivo json no seu Postman.
