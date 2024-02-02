FROM python:latest

RUN pip install --upgrade pip
RUN pip install poetry

COPY ../pyproject.toml /workspace/pyproject.toml
WORKDIR /workspace
RUN poetry install
