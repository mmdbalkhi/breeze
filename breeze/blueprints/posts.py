from breeze.auth import Auth
from breeze.forms import PostForm
from breeze.models import Comment
from breeze.models import Post
from breeze.utils import get_current_time
from breeze.utils import get_image_from_gravatar
from flask import abort
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

auth = Auth()
bp = Blueprint("posts", __name__, url_prefix="/p")


@bp.route("/new", methods=("GET", "POST"))
def new():
    """Create a new post

    :returns:
        :class:`flask.Response`: The rendered template if the request is GET,
        :class:`flask.Response`: The redirect to the post if the request is POST
    """
    form = PostForm()

    if not auth.is_authenticated:
        flash("You must be logged in to create a post")
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        if not form.validate_on_submit():  # pragma: no cover
            flash("please fill out all fields", "error")
            return render_template("posts/new.html", form=form), 400

        user_id = session["user_id"]

        content = request.form["content"]
        post = Post(
            user_id=user_id,
            content=content,
            time=get_current_time().strftime("%Y-%m-%d %H:%m:%S"),
        )
        post.save()
        flash("Post created successfully.")
        return redirect(f"/p/{post.id}")

    return render_template("posts/new.html", form=form)


@bp.route("/<int:id>")
def show(id: int):
    """Show a post

    :args:
        ``id`` (`int`): The id of the post to show

    :returns:
        :class:`flask.Response`: The rendered template
    """
    post = Post.get_post_by_id(id)
    comments = Comment.get_comments_by_post_id(id)
    if not post:
        abort(404)

    return render_template(
        "posts/show.html",
        gravatar=get_image_from_gravatar,
        post=post,
        comments=comments,
    )


@bp.route("/<int:id>/delete")
def delete(id: int):
    """Delete a post

    :args:
        ``id`` (`int`): The id of the post to delete

    :returns:
        :class:`flask.Response`: The redirect to the home page
    """
    user_id = request.cookies.get("user_id")

    post = Post.get_post_by_id(id)
    if not post:
        abort(404)

    if not auth.is_authenticated:
        flash("You must be logged in to delete a post")
        return redirect(url_for("auth.login"))

    if post.user_id != int(user_id):
        flash("You are not authorized to delete this post")
        return redirect(url_for("posts.show", id=id))

    post.delete()
    flash("Post deleted successfully.")
    return redirect(url_for("index"))
