""" a flask application similar to Twitter just for fun!
"""
import logging
from pathlib import Path

from breeze import utils
from breeze.auth import Auth
from breeze.commands import create_admin
from breeze.commands import create_db
from breeze.commands import drop_db
from breeze.config import BreezeConfig
from breeze.exc import BreezeException
from breeze.models import Comment
from breeze.models import db
from breeze.models import Post
from breeze.models import Tag
from breeze.models import User
from flask import Flask

__version__ = "0.1.0-dev"


def create_app():
    """create a flask application with application Factory pattern
    `application Factory <https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/>`_

    :return:
        :class:`flask.Flask`: flask application
    """

    app = Flask(__name__)
    app.config.from_object("breeze.Config")

    # register database
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # register app(s) from blueprints

    return app


class Config(BreezeConfig):
    """breeze configuration
    Inherit from :class:`breeze.BreezeConfig`

    """

    import os

    from dotenv import find_dotenv, load_dotenv

    dotenv_path = find_dotenv()
    if not dotenv_path:
        logging.warning(".env not found")
        Path(".env").touch()
    load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY")

    DEBUG = True
