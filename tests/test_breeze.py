from pathlib import Path

from breeze import create_app
from flask import Flask


def test_create_app():
    assert isinstance(create_app(), Flask)


def test_create_app_if_db_is_exists():
    path = Path("breeze/breeze.db")
    path.touch()
    assert isinstance(create_app(), Flask)
