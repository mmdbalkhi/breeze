from flask import Blueprint
from flask import render_template

from breeze.models import Post

bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    """Render the index page

    :returns:
        :class:`flask.Response`: The rendered template
    """
    posts = Post.get_all_posts()
    return render_template("index.html", posts=posts)
