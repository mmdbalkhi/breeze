import pytest
from sqlalchemy.exc import IntegrityError

from . import TestBreezeDB
from breeze import exc
from breeze.models import Post
from breeze.models import User
from breeze.utils import get_current_time


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

    def test_check_password(self):
        with self.app.app_context():
            user = User(
                username="testcheckpassword",
                email="testcheckpassword@test.com",
                password="testcheckpassword",
            )
            user.save()

            user = User.query.filter_by(username="testcheckpassword").first()
            assert user.check_password("testcheckpassword")
            assert not user.check_password("testcheckpassword2")


class TestPost(TestBreezeDB):
    def test_create_post(self):
        with self.app.app_context():
            user = User(username="test1", email="test1@test.com", password="test1")
            user.save()
            post = Post(
                content="test1",
                user_id=user.id,
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )
            post.save()

    def test_remove_post(self):
        with self.app.app_context():
            post = Post.get_post_by_id(1)
            post.delete()
