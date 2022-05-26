import pytest
from breeze import exc
from breeze.models import Comment
from breeze.models import Post
from breeze.models import User
from breeze.utils import get_current_time
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
            assert str(user1) == "User('test1', 'test1@test.com')"

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

            user = User.get_user_by_username(username="testcheckpassword")
            assert user.check_password("testcheckpassword")
            assert not user.check_password("testcheckpassword2")

    def test_get_user_by_id(self):
        with self.app.app_context():
            assert User.get_user_by_id(1)


class TestPost(TestBreezeDB):
    def test_create_post(self):
        with self.app.app_context():
            user = User(
                username="test_create_post",
                email="test_create_post@test.com",
                password="test_create_post",
            )
            user.save()
            post = Post(
                content="test_create_post",
                user_id=user.id,
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )
            post.save()
            assert post.id == 1
            assert post.content == "test_create_post"
            assert (
                str(post)
                == "Post('User('test_create_post', 'test_create_post@test.com')', 'test_create_post')"  # noqa: B950
            )

    def test_remove_post(self):
        with self.app.app_context():
            user = User(
                username="test_remove_post",
                email="test_remove_post@test.com",
                password="test_remove_post",
            )
            user.save()
            post = Post(
                content="test_remove_post",
                user_id=user.id,
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )
            post.save()
            post.delete()

    def test_delete_post(self):
        with self.app.app_context():
            post = Post.get_post_by_id(1)
            post.delete()


class TestComment(TestBreezeDB):
    def test_create_comment(self):
        with self.app.app_context():

            user = User(
                username="test_create_comment",
                email="test_create_comment@test.com",
                password="test_create_comment",
            )
            user.save()

            post = Post(
                user=user,
                content="test1",
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )
            post.save()

            comment = Comment(
                user=user,
                post=post,
                content="test comments",
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )
            comment.save()

            assert comment.id == 1
            assert comment.content == "test comments"
            assert str(comment) == "Comment(1, 'test comments')"

    def test_delete_comment(self):
        with self.app.app_context():

            user = User(
                username="test_delete_comment",
                email="test_delete_comment@test.com",
                password="test_delete_comment",
            )
            user.save()

            post = Post(
                user=user,
                content="test1",
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )

            post.save()
            comment = Comment(
                user=user,
                post=post,
                content="test comments",
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )
            comment.save()

            comment = Comment.get_comment_by_id(post.id)
            comment.delete()

            assert not Comment.get_comment_by_id(post.id)

    def test_get_comment_by_user_id(self):
        with self.app.app_context():
            user = User(
                username="test_get_comment_by_user_id",
                email="test_get_comment_by_user_id@test.com",
                password="test_get_comment_by_user_id",
            )
            user.save()
            post = Post(
                user=user,
                content="test_get_comment_by_user_id",
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )
            post.save()
            comment = Comment(
                user=user,
                post=post,
                content="test_get_comment_by_user_id",
                time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            )

            assert Comment.get_comments_by_user_id(user.id)[0] == comment
