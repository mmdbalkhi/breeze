<p algin="center">
    <img src="https://raw.githubusercontent.com/mmdbalkhi/breeze/main/artwork/breeze.png">
</p>

<h5 align="center"> a flask application similar to Twitter just For Fun!</h5>

<p align="center">
    <a href="https://github.com/mmdbalkhi/breeze/tree/main/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg">
    </a>
    <a href='https://python-breeze.readthedocs.io/?badge=latest'>
        <img src='https://readthedocs.org/projects/python-breeze/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://github.com/mmdbalkhi/breeze/actions/workflows/tests.yaml">
        <img src="https://github.com/mmdbalkhi/breeze/actions/workflows/tests.yaml/badge.svg"
        alt="test badge">
    </a>
    <a href="https://codecov.io/gh/mmdbalkhi/breeze">
        <img src="https://codecov.io/gh/mmdbalkhi/breeze/branch/main/graph/badge.svg?token=6C8nLeyYht"/>
    </a>
</p>

the breeze is a fun web application for practising with [Flask](https://flask.palletsprojects.com/), [SQLalchemy](https://www.sqlalchemy.org/) and a few other things that try to be similar to **Twitter**!

## Run

* install required packages

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

* add breeze to environment

```bash
export FLASK_APP=breeze
```

* run server

```bash
flask run
```
