from breeze import GithubOAuth2
from breeze.auth import Auth
from breeze.forms import LoginForm
from breeze.forms import RegisterForm
from breeze.models import Post
from breeze.models import User
from breeze.utils import get_image_from_gravatar
from breeze.utils import normalise_email
from flask import abort
from flask import Blueprint
from flask import current_app
from flask import flash
from flask import g
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

auth = Auth()
bp = Blueprint("auth", __name__, url_prefix="/u")
gh = GithubOAuth2()


@bp.before_app_request
def load_logged_in_user():
    """If a `user_id` set in the cookie, load the user object into `g.user`"""
    user_id = request.cookies.get("user_id")
    if user_id is None:
        if session.get("user_id") is None:
            g.user = None
        else:
            g.user = User.query.get(session["user_id"])
    else:
        session["user_id"] = user_id
        g.user = User.query.get(user_id)


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user to the system.

    :returns:
        :class:`flask.Response`:
            - method Get:
                render the register template
            - method Post:
                register the user and redirect to the login page

    """
    form = RegisterForm(request.form)

    if request.method == "POST":
        if not form.validate_on_submit():  # pragma: no cover
            flash("please fill out all fields")
            return render_template("auth/register.html", form=form), 400

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        profile_image = get_image_from_gravatar(email)

        if password != confirm_password:
            error = "passwords do not match"
        elif User.query.filter_by(username=username).first():
            error = f"User {username} is already registered."
        else:
            email = normalise_email(email)
            if not email:
                flash("email is invalid")
                return (
                    render_template("auth/register.html", form=form),
                    400,
                )
            if User.get_user_by_email(email):
                flash("email is already registered")
                return (
                    render_template("auth/register.html", form=form),
                    400,
                )

            user = User(
                username=username,
                email=email,
                password=password,
                profile_image=profile_image,
            )
            auth.register(user)

            resp = make_response(redirect(url_for("index")))
            resp.set_cookie(
                "user_id",
                str(user.id),
                max_age=60 * 60 * 24 * 7,
                secure=False if current_app.config.get("TESTING") else True,
            )
            return resp

        flash(error)
        return (
            render_template("auth/register.html", form=form),
            400,
        )

    return render_template("auth/register.html", form=form)


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Login a user to the system.

    :returns:
        :class:`flask.Response`:
            - if the request method is GET, render the login template
            - if the request method is POST, login the user and redirect to the index page
    """
    form = LoginForm(request.form)

    if request.method == "POST":
        if not form.validate_on_submit():  # pragma: no cover
            flash("please fill out all fields")
            return render_template("auth/login.html", form=form), 400

        username = request.form.get("username")
        password = request.form.get("password")
        remember_me = request.form.get("remember_me")

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash("Incorrect username or password.")
            return (
                render_template("auth/login.html", form=form),
                401,
            )

        max_age = 7 * 24 * 60 * 60  # 7 days
        if remember_me:  # pragma: no cover
            session.permanent = True
            max_age = 365 * 24 * 60 * 60  # one year

        auth.login(user)
        resp = make_response(redirect(url_for("index")))
        resp.set_cookie("user_id", str(user.id), max_age=max_age, secure=True)
        return resp
    return render_template(
        "auth/login.html",
        form=form,
    )


@bp.route("/logout")
def logout():
    """Logout a user from the system.

    :returns:
        :class:`flask.Response`: redirect to the login page
    """
    resp = make_response(redirect(url_for("auth.login")))
    resp.delete_cookie("user_id")
    flash("You have been logged out.")
    auth.logout()
    return resp


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
    img = user.profile_image
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


@bp.route("/github")
def github():
    """redirect to auth url"""
    return redirect(gh.create_authorization_data()[0])
