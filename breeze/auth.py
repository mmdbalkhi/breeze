from functools import wraps

from breeze.models import db
from breeze.models import User
from flask import g
from flask import session


class Auth:
    """Authentication class for Breeze

    Attributes:
        :attr:`User` (class): User class
    """

    def __init__(self, app=None):
        """Initialize the authentication class

        Args:
            ``app`` (:class:`flask.Flask`, optional): Defaults to None.
        """
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the authentication class with the app

        Args:
            ``app`` (:class:`flask.Flask`): flask application
        """
        app.config.setdefault("AUTH_USER_MODEL", User)
        self.User = app.config["AUTH_USER_MODEL"]

    def login_required(self, func):
        """Decorator to require login

        Args:
            ``func`` (`function`): a function to be decorated

        Returns:
            ``decorator``: a decorator to require login
        """

        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not self.current_user:
                return self.login_manager.unauthorized()
            return func(*args, **kwargs)

        return decorated_view

    @property
    def current_user(self):
        """Get the current user

        Returns:
            :class:`flask.g`: flask global object
        """
        if not hasattr(g, "user"):
            g.user = None
            if "user_id" in session:
                g.user = self.User.query.get(session["user_id"])
        return g.user

    @property
    def is_authenticated(self):
        """Check if the user is authenticated

        Returns:
            `bool`: if current user is authenticated
        """
        return self.current_user is not None

    def login(self, user):
        """Login the user to the session

        Args:
            `User` (:class`breeze.User`): user row in db
        """
        session["user_id"] = user.id
        g.user = user

    def logout(self):
        """Logout the user from the session"""
        session.pop("user_id", None)
        g.user = None

    def register(self, user):
        """Register the user to the db

        Args:
            `user` (:class:`breeze.User`): user row in db
        """
        db.session.add(user)
        db.session.commit()
        self.login(user)

    def get_user(self, user_id):
        """Get the user by id

        Args:
            ``user_id`` (:meth:`breeze.User.id`): user id

        Returns:
            :class:`breeze.User`: user row in db
        """
        return self.User.query.get(user_id)
