from breeze.auth import Auth
from breeze.models import Post
from breeze.models import User
from breeze.utils import get_image_from_gravatar
from breeze.utils import normalise_email
from flask import abort
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

bp = Blueprint("auth", __name__, url_prefix="/u")
auth = Auth()


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")
    user = User()
    if user_id is None:
        g.user = None
    else:
        g.user = user.get_user_by_id(id=user_id)


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
            email = normalise_email(email)
            if not email:
                flash("email is invalid")
                return (
                    render_template(
                        "auth/register.html",
                    ),
                    400,
                )

            user = User(username=username, email=email, password=password)
            auth.register(user)

            flash("Registered successfully.")
            return redirect(url_for("auth.login"))

        flash(error)
        return (
            render_template(
                "auth/register.html",
            ),
            400,
        )

    return render_template(
        "auth/register.html",
    )


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
            error, status_code = "Username and password are required.", 400
        else:
            user = User.query.filter_by(username=username).first()
            if not user or not user.check_password(password):
                error, status_code = "Incorrect username or password.", 401

        if error is None:
            auth.login(user)
            return redirect(url_for("auth.profile"))

        flash(error)
        return (
            render_template(
                "auth/login.html",
            ),
            status_code,
        )

    return render_template(
        "auth/login.html",
    )


@bp.route("/logout")
def logout():
    """Logout a user from the system.

    :returns:
        :class:`flask.Response`: redirect to the login page
    """
    flash("You have been logged out.")
    auth.logout()
    return redirect(url_for("auth.login"))


@bp.route("/<username>")
def user(username: str):
    """Show a user's profile.

    :args:
        ``username`` (`str`): The username of the user to show

    :returns:
        :class:`flask.Response`: The rendered template
    """
    user = User.get_user_by_username(username)
    if not user:
        abort(404)
    img = get_image_from_gravatar(user.email)
    posts = Post.get_posts_by_user_id(user.id)
    return render_template(
        "auth/user.html",
        username=username,
        img=img,
        posts=posts,
    )


@bp.route("/profile")
def profile():
    """Show the current user's profile.

    :returns:
        :class:`flask.Response`: redirect to the user's profile to /u/username
    """
    if auth.is_authenticated:
        user_id = session["user_id"]
        username = User.get_user_by_id(user_id).username
        return redirect(f"/u/{username}")

    flash("you must be logged in to see your profile")
    return redirect(url_for("auth.login"))
