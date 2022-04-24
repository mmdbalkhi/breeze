<p algin="center">
    <img src="artwork/breeze.svg">
</p>

<h5 align="center"> a flask application similar to Twitter just For Fun!</h5>

<p align="center">
    <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
</p>

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
