from breeze import Auth
from breeze import GithubOAuth2
from breeze.models import User
from breeze.utils import gen_random_string
from flask import abort
from flask import Blueprint
from flask import redirect
from flask import request
from flask import url_for

auth = Auth()

bp = Blueprint("callback", __name__, url_prefix="/c")
gh = GithubOAuth2()


@bp.route("/github")
def github():  # pragma: no cover
    """Github OAuth2 callback

    this function is called by Github OAuth2 after user has authorized the app.

    :returns:
        :class:`flask.Response`:

    .. note::
        this function for now can't be tested because it's need to Auth user to get token
    """

    code = request.args.get("code")
    state = request.args.get("state")

    if not (code and state):
        abort(400)

    access_token = gh.fetch_token(
        f"{request.url_root}c/github?{request.query_string.decode('utf-8')}"
    )
    if access_token is None:
        abort(400)

    user_info = gh.get_user_info(access_token)
    if user_info is None:
        abort(400)

    user = User.query.filter_by(username=user_info["login"]).first()
    if user is None:
        user = User(
            username=user_info["login"],
            email=user_info["email"],
            password=gen_random_string(length=32),
            profile_image=user_info["avatar_url"],
        )
        auth.register(user)
    else:
        auth.login(user)

    return redirect(url_for("index"))
