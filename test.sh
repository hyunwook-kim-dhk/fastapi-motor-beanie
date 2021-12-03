#!/usr/bin/env bash
set -euo pipefail

source .venv/bin/activate

echo "Starting flake8"
poetry run flake8 app tests
echo "OK"

echo "Starting black"
poetry run black --check app tests
echo "OK"

echo "Starting isort"
poetry run isort . --check --diff
echo "OK"

echo "Starting pylint"
poetry run pylint app tests
echo "OK"

echo "Starting mypy"
poetry run mypy app tests
echo "OK"

echo "Starting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
echo "OK"

echo "All tests passed successfully!"
