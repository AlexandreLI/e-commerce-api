coverage:
	python -m pytest -v --cov-report term-missing --cov=src/ --cov-report=html --cov-config=.coveragerc

test:
	python -m pytest

fixtures:
	python manage.py loaddata src/django_project/fixtures/initial_data.json

migrate:
	python manage.py migrate

run:
	python manage.py runserver