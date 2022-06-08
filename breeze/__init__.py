""" a flask application similar to Twitter just for fun!
"""
from breeze import exc
from breeze import utils
from breeze.auth import Auth
from breeze.blueprints import auth as auth_bp
from breeze.blueprints import comments as comments_bp
from breeze.blueprints import index as index_bp
from breeze.blueprints import posts as posts_bp
from breeze.config import Config
from breeze.models import Comment
from breeze.models import db
from breeze.models import Post
from breeze.models import Tag
from breeze.models import User

__version__ = "0.5.0-dev"


def create_app(test_config=None):
    """create a flask application with application Factory pattern
    `application Factory <https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/>`_

    :return:
        :class:`flask.Flask`: flask application
    """
    from flask import Flask, json
    from flask_wtf import CSRFProtect
    from werkzeug.exceptions import HTTPException
    from sqlalchemy.exc import OperationalError

    csrf = CSRFProtect()

    # init flask app
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        # static_folder="../frontend/static",
    )

    app.config.from_object("breeze.Config")
    csrf.init_app(app)

    with app.app_context():

        try:
            # init database
            db.init_app(app)
            db.create_all()
        except OperationalError:  # pragma: no cover
            pass
    app.config["TESTING"] = True
    if test_config:
        app.config.update(test_config)
        app.config["WTF_CSRF_ENABLED"] = False

    # register app(s) from blueprints
    app.register_blueprint(auth_bp.bp)
    app.register_blueprint(comments_bp.bp)
    app.register_blueprint(index_bp.bp)
    app.register_blueprint(posts_bp.bp)

    # add rule to bp(s)
    app.add_url_rule("/", endpoint="index")

    return app
