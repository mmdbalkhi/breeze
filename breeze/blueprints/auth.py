from breeze.auth import Auth
from breeze.models import User
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

bp = Blueprint("auth", __name__)
auth = Auth()


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user to the system.

    :returns:
        :class:`flask.Response`:
            - if the request method is GET, render the register template
            - if the request method is POST, register the user and redirect to the login page

    """
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            error = "please fill out all fields"
        elif User.query.filter_by(username=username).first():
            error = f"User {username} is already registered."

        else:
            user = User(username=username, email=email, password=password)
            auth.register(user)

            flash("Registered successfully.")
            return redirect(url_for("auth.login"))

        flash(error)
        return render_template("auth/register.html"), 400

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Login a user to the system.

    :returns:
        :class:`flask.Response`:
            - if the request method is GET, render the login template
            - if the request method is POST, login the user and redirect to the index page
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username or not password:
            error = "Username and password are required."
        else:
            user = User.query.filter_by(username=username).first()
            if not user or not user.check_password(password):
                error = "Incorrect username or password."

        if error is None:
            auth.login(user)
            return redirect(url_for("auth.index"))

        flash(error)
        return render_template("auth/login.html"), 400

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Logout a user from the system.

    :returns:
        :class:`flask.Response`: redirect to the login page
    """
    flash("You have been logged out.")
    auth.logout()
    return redirect(url_for("auth.index"))


@bp.route("/")
def index():
    return render_template("index.html")
