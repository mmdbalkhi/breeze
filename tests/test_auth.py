from breeze import Auth
from breeze import db
from breeze import User
from flask import g
from flask import session

from . import TestBreezeDB

auth = Auth()


class TestAuth(TestBreezeDB):
    """Test the Auth class"""

    def test_init_app(self):
        """Test the init_app method"""
        with self.app.app_context():
            auth.init_app(self.app)

    def test_register(self):
        """Test the register method"""
        with self.app.app_context():
            # Ensure that the database is empty
            db.drop_all()
            db.create_all()

            @self.app.route("/register")
            def register():
                # Create a user
                user = User(username="test", email="test@test.com", password="test")

                # register user to db
                auth.register(user)

                return "OK"

            assert self.client.get("/register").status_code == 200

    def test_login(self):
        """Test the login method"""
        with self.app.app_context():
            # Ensure that the database is empty
            db.drop_all()
            db.create_all()

            @self.app.route("/login")
            def login():
                # Create a user
                user = User(username="test", email="test@test.com", password="test")
                user.save()

                # Login the user
                auth.login(user)

                assert g.user == user
                assert session["user_id"] == user.id

                return "OK"

        assert self.client.get("/login").status_code == 200

    def test_logout(self):
        """Test the logout method"""
        with self.app.app_context():
            # Ensure that the database is empty
            db.drop_all()
            db.create_all()

            @self.app.route("/logout")
            def logout():
                # Create a user
                user = User(username="test", email="test@test.com", password="test")
                user.save()

                # Login the user
                auth.login(user)

                # Logout the user
                auth.logout()

                return "OK"

        assert self.client.get("/logout").status_code == 200

    def test_current_user(self):
        with self.app.app_context():
            # Ensure that the database is empty
            db.drop_all()
            db.create_all()

            @self.app.route("/current_user")
            def current_user():
                user = User(username="test", email="test@test.com", password="test")
                auth.login(user)

                return str(auth.current_user)

            assert (
                self.client.get("/current_user").data
                == b"User('test', 'test@test.com')"
            )

    def test_is_authenticated(self):
        """Test the is_authenticated property"""
        with self.app.app_context():

            @self.app.route("/is_auth")
            def is_auth():
                # Create a user
                # Ensure that the database is empty
                db.drop_all()
                db.create_all()

                # Create a user
                user = User(username="test", email="test@test.com", password="test")
                user.save()

                # Login the user
                auth.login(user)

                # Check if the user is authenticated
                assert auth.is_authenticated

                return "OK"

            assert self.client.get("/is_auth").status_code == 200

    def test_get_user(self):
        with self.app.app_context():
            # Ensure that the database is empty
            db.drop_all()
            db.create_all()

            user = User(username="test", email="test@test.com", password="test")
            user.save()
            assert str(auth.get_user(user.id)) == "User('test', 'test@test.com')"
