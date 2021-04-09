# docker build . -t typicode
# docker run -p 8000:8000 -v $(pwd):/var/app:z typicode
FROM python:3.8-buster

WORKDIR /var/app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
