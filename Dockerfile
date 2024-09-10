FROM python:3.12.3-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y

ADD ./src/ ./
WORKDIR /app/

# Copia o arquivo pyproject.toml e poetry.lock separadamente
COPY pyproject.toml poetry.lock ./
COPY manage.py ./

# Update pip
RUN pip install -U pip

# Poetry install
RUN pip install poetry  \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev


CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]