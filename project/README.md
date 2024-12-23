# Project FastApi Learning

## Dependencies

* FastApi
* Ruff
* PyTest
* PyTest-cov
* Taskipy
* pydantic[email]

## Install dependencies

    poetry add fastapi[standard]
    poetry add --group dev ruff
    poetry add --group dev pytest pytest-cov
    poetry add --group dev taskipy
    poetry add "pydantic[email]"

## PyTest Commands

    pytest          //Initialize test
    coverage html   //Making an html page from test

### Poetry Configuration

    [tool.pytest.init_options]
    pythonpath = '.'
    addopts = '-p no:warnings'

## Ruff commands

    ruff check .        //The checked Lines are not in conformance
    ruff check . --fix  //Update Lines for conformance
    ruff format .       //Update Lines for formattion conformance
    

### Linter commands 

* I (Isort)         : Ordenação de imports em ordem alfabetica
* F (Pyflakes)      : Procura por alguns erros em relações a boas práticas
* E (pycodestyle)   : Erros de estilo de código
* W (pycodestyle)   : Avisos sobre estilo de código
* PL (PyLint)       : "Erros" em relação a boas práticas de código
* PT (flake8=pytest): Boas práticas do Pytest
### Poetry configuration

        [tool.ruff]
        line-length = 79
        extend-exclude = ['migrations']

        [tool.ruff.format]
        preview = true
        quote-style = 'single'

        [tool.ruff.lint]
        preview = true
        select = ['I', 'F', 'E', 'W', 'PL', 'PT']

## Taskipy commands

    tasking <command>

### Poetry configurarion

    [tool.taskipy.tasks]
    run = 'fastapi dev api/app.py'
    test = 'pytest -s -x --cov=aou -vv'
    post_test = 'converage html'


## Initialize project

- Dev

        fastapi dev ./app.py

- Release

        uvicorn app:app --reload --port 8080