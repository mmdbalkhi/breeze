from breeze import Auth
from breeze import exc
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
    """Register a new user to the system

    :returns:
        :class:`flask.Response`: The response to the request
    """
    if request.method == "POST":
        username = request.args.get("username")
        email = request.args.get("email")
        password = request.args.get("password")

        try:
            user = User(username=username, email=email, password=password)
            auth.register(user)
        except exc.EmptyError as e:
            flash(e.message)
            return redirect(url_for("auth.register"))
    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Login a user to the system

    :returns:
        :class:`flask.Response`: The response to the request
    """
    if request.method == "POST":
        username = request.args.get("username")
        password = request.args.get("password")

        try:
            user = User.query.filter_by(username=username).first()

            if not user.check_password(password):
                flash("password is not correct")

            auth.login(user)
            return redirect(url_for("index"))
        except exc.EmptyError as e:
            flash(e.message)
            return redirect(url_for("auth.login"))
    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Logout a user from the system

    :returns:
        :class:`flask.Response`: The response to the request
    """
    auth.logout()
    return redirect(url_for("index"))
