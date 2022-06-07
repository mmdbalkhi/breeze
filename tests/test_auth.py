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

    def test_current_user_if_not_g(self):
        @self.app.route("/current_user_if_not_g")
        def current_user_if_not_g():

            # login the user
            user = User(username="test", email="test@test.com", password="test")
            user.save()

            auth.login(user)

            # remove user attribute from g
            delattr(g, "user")

            # add user_id to session
            session["user_id"] = user.id

            return str(auth.current_user)

        assert (
            self.client.get("/current_user_if_not_g").data
            == b"User('test', 'test@test.com')"
        )

        @self.app.route("/current_user_if_not_g_not_session")
        def current_user_if_not_g_not_session():
            session.pop("user_id")  # remove user_id from session
            return str(auth.current_user)

        assert self.client.get("/current_user_if_not_g_not_session").data == b"None"

    def test_is_authenticated(self):
        """Test the is_authenticated property"""
        with self.app.app_context():

            @self.app.route("/is_auth_true")
            def is_auth_true():
                # Create a user
                # Ensure that the database is empty
                db.drop_all()
                db.create_all()

                user = User(username="test", email="test@test.com", password="test")
                auth.login(user)

                # Check if the user is authenticated
                assert auth.is_authenticated

                return str(auth.is_authenticated)

            @self.app.route("/is_auth_false")
            def is_auth_false():
                # Create a user
                # Ensure that the database is empty
                db.drop_all()
                db.create_all()

                # logout the user
                auth.logout()

                # Check if the user is authenticated
                assert not auth.is_authenticated

                return str(auth.is_authenticated), 401

            # if user is authenticated
            assert self.client.get("/is_auth_true").status_code == 200
            assert self.client.get("/is_auth_true").data == b"True"

            # if user is not authenticated
            assert self.client.get("/is_auth_false").status_code == 401
            assert self.client.get("/is_auth_false").data == b"False"

    def test_get_user(self):
        with self.app.app_context():
            # Ensure that the database is empty
            db.drop_all()
            db.create_all()

            user = User(username="test", email="test@test.com", password="test")
            user.save()
            assert str(auth.get_user(user.id)) == "User('test', 'test@test.com')"
