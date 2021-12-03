FROM python:3.9.6

RUN pip install "poetry==1.1.7"

WORKDIR /fastapi-motor-skeleton
COPY poetry.lock pyproject.toml ./
COPY app ./app

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

CMD ["uvicorn", "app.start:app", "--host", "0.0.0.0", "--port", "80"]
