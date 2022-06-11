""" a flask application similar to Twitter just for fun!
"""
from breeze import exc
from breeze import utils
from breeze.auth import Auth
from breeze.auth import GithubOAuth2
from breeze.blueprints import auth as auth_bp
from breeze.blueprints import callback as callback_bp
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
    from authlib.integrations.base_client.errors import OAuthError
    from flask import Flask, json, render_template
    from flask_wtf import CSRFProtect
    from sqlalchemy.exc import OperationalError
    from werkzeug.exceptions import HTTPException

    csrf = CSRFProtect()

    # init flask app
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        # static_folder="../frontend/static",
    )

    app.config.from_object("breeze.Config")
    csrf.init_app(app)

    # check app is running in production mode
    if test_config:  # pragma: no cover
        # set test config
        app.config.update(test_config)
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False  # if when testing Debug is on, some tests will fail

    with app.app_context():
        try:
            # init database
            db.init_app(app)
            db.create_all()
        except OperationalError:  # pragma: no cover
            pass

    # register error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template("errors/405.html"), 405

    # register app(s) from blueprints
    app.register_blueprint(auth_bp.bp)
    app.register_blueprint(callback_bp.bp)
    app.register_blueprint(comments_bp.bp)
    app.register_blueprint(index_bp.bp)
    app.register_blueprint(posts_bp.bp)

    # add rule to bp(s)
    app.add_url_rule("/", endpoint="index")

    app.add_url_rule("/register", endpoint="auth.register")
    app.add_url_rule("/login", endpoint="auth.login")
    app.add_url_rule("/logout", endpoint="auth.logout")

    return app
