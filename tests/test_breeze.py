from breeze import create_app
from flask import Flask


def test_create_app():
    assert isinstance(create_app(), Flask)
