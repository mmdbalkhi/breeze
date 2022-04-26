import unittest

import pytest
from flask import Flask
from sqlalchemy.exc import IntegrityError

from breeze import User, db, exc


class TestBreezeDB(unittest.TestCase):

    # initial flask app
    app = Flask(__name__)

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


class UserTests(TestBreezeDB):
    def test_create_user(self):
        """
        Adds test data to the database
        """
        with self.app.app_context():
            user1 = User(username="test1", email="test1@test.com", password="test1")
            user1.save()
            user2 = User(username="test2", email="test2@test.com", password="test2")
            user2.save()

    def test_duplicate_user_error(self):
        with pytest.raises(IntegrityError), self.app.app_context():
            user = User(username="test1", email="test3@test.com", password="qwerty")
            user.save()

    def test_duplicate_email_error(self):
        with pytest.raises(IntegrityError), self.app.app_context():
            user = User(username="test3", email="test1@test.com", password="qwerty")
            user.save()

    def test_empty_password_error(self):
        with pytest.raises(exc.EmptyError), self.app.app_context():
            user = User(username="test3", email="test3@test.com")
            user.save()

    def test_remove_user(self):
        with self.app.app_context():
            user = User(username="test1", email="test1@test.com", password="test1")
            user.delete(confirm_password="test1")

    def test_remove_user_permission_error(self):
        with pytest.raises(exc.PermissionError), self.app.app_context():
            user = User(username="test2", email="test2@test.com")
            user.delete(confirm_password="abcd")
