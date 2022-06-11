from pathlib import Path

from breeze import create_app
from flask import Flask


def test_create_app():
    assert isinstance(create_app(), Flask)


def test_create_app_if_db_is_exists():
    path = Path("breeze/breeze.db")
    path.touch()
    assert isinstance(create_app(), Flask)


def test_404_page(client):
    response = client.get("/404")
    assert response.status_code == 404
    assert b"404" in response.data


def test_405_page(client):
    response = client.put("/")  # method not allowed
    assert response.status_code == 405
    assert b"405" in response.data
