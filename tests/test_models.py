import pytest
from breeze import exc
from breeze import User
from sqlalchemy.exc import IntegrityError

from . import TestBreezeDB


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
            user = User(username="test1", email="test1@test.com")
            user.delete(confirm_password="test1")

    def test_remove_user_permission_error(self):
        with pytest.raises(exc.PermissionError), self.app.app_context():
            user = User(username="test2", email="test2@test.com")
            user.delete(confirm_password="abcd")
