from flask import Flask

from breeze import create_app


def test_create_app():
    assert isinstance(create_app(), Flask)
