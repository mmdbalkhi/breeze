""" a flask application similar to Twitter just for fun!
"""

from flask import Flask

from breeze import utils
from breeze.auth import Auth
from breeze.commands import create_admin, create_db, drop_db
from breeze.config import Config
from breeze.exc import BreezeException
from breeze.models import Comment, Post, Tag, User, db

__version__ = "0.1.0-dev"


def create_app():
    app = Flask(__name__)
    app.config.from_object("breeze.BreezeConfig")

    # register database
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # register app(s) from blueprints

    return app


class BreezeConfig(Config):
    """load env variables from .env file"""

    import os

    from dotenv import find_dotenv, load_dotenv

    dotenv_path = find_dotenv()
    if not dotenv_path:
        raise FileExistsError(".env file not exists.")
    load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY")

    DEBUG = True
