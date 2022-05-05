import unittest

from flask import Flask

from breeze import db


class TestBreezeDB(unittest.TestCase):
    """Parrent class for all tests by need to init flask app"""

    # initial flask app
    app = Flask(__name__)
    client = app.test_client()

    # flask app configs
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "very Secret key"

    # SQLAlchemy configs
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///breeze.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.init_app(app)

        # Ensures that the database is emptied for next unit test
        db.drop_all()

        db.create_all()
