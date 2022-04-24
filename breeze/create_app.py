import os
from typing import Callable

from dotenv import find_dotenv, load_dotenv
from flask import Flask

from breeze import BreezeConfig


def create_app(test_config=None) -> Callable:
    """Create and configure an instance of the Flask application.

    Args:
        test_config (str, optional): test configs. Defaults to None.

    Returns:
        Callable: a flask app
    """
    app = Flask(__name__)
    app.config.from_object("breeze.create_app.BreezeConfig")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # register app(s) from blueprints

    return app
