from breeze.auth import Auth
from breeze.forms import PostForm
from breeze.models import Comment
from breeze.models import Post
from breeze.utils import get_current_time
from flask import abort
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

auth = Auth()
bp = Blueprint("comments", __name__, url_prefix="/p")


@bp.route("/<int:post_id>/new", methods=("GET", "POST"))
def new(post_id):
    """create a new comment
    :param post_id: post id
    :type post_id: int
    :return:
        :class:`flask.Response`: response
    """

    form = PostForm()

    post = Post.get_post_by_id(post_id)
    if not post:
        abort(404)

    if not auth.is_authenticated:
        return redirect(location=url_for("auth.login"))

    if request.method == "POST":

        if not form.validate_on_submit():  # pragma: no cover
            flash("please fill out all fields", "error")
            return render_template("comments/new.html", post=post, form=form), 400

        content = request.form.get("content")

        comment = Comment(
            content=content,
            time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
            user=g.user,
            post=post,
        )
        comment.save()

        return redirect(f"/p/{post_id}")

    return render_template("comments/new.html", post=post, form=form)
