# Project FastApi Learning

## Dependencies

* FastApi
* Ruff
* PyTest
* Taskipy

## Install Dependencies

    poetry add fastapi[standard]
    poetry add --group dev ruff

## Commands Linter Ruff

    * I(Isort)         : Ordenação de imports em ordem alfabetica
    * F(Pyflakes)      : Procura por alguns erros em relações a boas práticas
    * E(pycodestyle)   : Erros de estilo de código
    * W(pycodestyle)   : Avisos sobre estilo de código
    * PL(PyLint)       : "Erros" em relação a boas práticas de código
    * PT(flake8=pytest): Boas práticas do Pytest

## Ruff Poetry Configuration 

    * I(Isort)         : Ordenação de imports em ordem alfabetica
    * F(Pyflakes)      : Procura por alguns erros em relações a boas práticas
    * E(pycodestyle)   : Erros de estilo de código
    * W(pycodestyle)   : Avisos sobre estilo de código
    * PL(PyLint)       : "Erros" em relação a boas práticas de código
    * PT(flake8=pytest): Boas práticas do Pytest

## Initialize Project

- Dev

        fastapi dev ./app.py

- Release

        uvicorn app:app --reload --port 8080