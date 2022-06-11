from breeze import exc
from breeze.utils import get_image_from_gravatar
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model):
    """Users table on db

    inherited from :class:`flask_sqlalchemy.SQLAlchemy`

    :raises:
        :class:`breeze.exc.EmptyError`: if password is empty then raise this exception
        :class:`breeze.exc.PermissionError`: if user not have permission to perform
        an action then raise this exception

    :methods:
        :meth:`save`: save user to db
        :meth:`delete`: delete user from db
        :meth:`update`: update user from db

    :attributes:
        :attr:`username` (`str`): user username
        :attr:`email` (`str`): user email
        :attr:`password` (`str`): user password
        :attr:`profile_image` (`str`): user profile image
            this is a url to the image and by default it is a gravatar image

    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)  # len(sha512) == 128
    profile_image = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        """User representation

        :returns:
            `str`: User representation
                e.g. User(username="admin", email="admin@test.com")
        """
        return f"User('{self.username}', '{self.email}')"

    def save(self):
        """Save user to db

        :raises:
            :class:`breeze.exc.EmptyError`
        """
        if not self.password:
            raise exc.EmptyError("password is Empty")

        self.password = generate_password_hash(self.password)

        if self.profile_image is None:
            self.profile_image = get_image_from_gravatar(self.email)

        db.session.add(self)
        db.session.commit()

    def delete(self, confirm_password):
        """Delete user from db

        :args:
            ``confirm_password`` (`str`): user password to confirm delete

        :raises:
            :class:`breeze.exc.PermissionError`
        """
        user = self.get_user_by_email(self.email)
        self.password = User.query.filter_by(email=self.email).first().password
        if not check_password_hash(self.password, confirm_password):
            raise exc.PermissionError(message="Password is not correct")

        db.session.delete(user)
        db.session.commit()

    def check_password(self, password):
        """Check user password

        :args:
            ``password`` (`hash`): User password to confirm delete

        :return: `bool`: True if password is correct, False otherwise
        """
        return check_password_hash(self.password, password)

    # id, username, email is unique
    @staticmethod
    def get_user_by_id(id):
        return User.query.filter_by(id=id).first()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()


class Post(db.Model):
    """Posts table on db

    inherited from :class:`flask_sqlalchemy.SQLAlchemy`

    :methods:
        :meth:`save`: save post to db
        :meth:`delete`: delete post from db
        :meth:`update`: update post from db
    """

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("posts", lazy=True))

    def __repr__(self):
        """Post representation

        :returns:
            `str`: Post representation
                e.g Post(user="mmdbalkhi", content="Hello World")
        """
        return f"Post('{self.user}', '{self.content}')"

    def save(self):
        """Save post to db"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete post from db"""
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_posts():
        return Post.query.all()

    @staticmethod
    def get_post_by_id(id):
        return Post.query.get(id)

    @staticmethod
    def get_posts_by_user_id(user_id):
        return Post.query.filter_by(user_id=user_id).all()


class Comment(db.Model):
    """"""

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("comments", lazy=True))

    post = db.relationship("Post", backref=db.backref("comments", lazy=True))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)

    def __repr__(self):
        return f"Comment({self.id}, '{self.content}')"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_comment_by_id(id):
        return Comment.query.get(id)

    @staticmethod
    def get_comments_by_user_id(user_id):
        return Comment.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_comments_by_post_id(post_id):
        return Comment.query.filter_by(post_id=post_id).all()


class Tag(db.Model):  # pragma: no cover
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Tag('{self.name}')"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name):
        self.name = name
        db.session.commit()

    @staticmethod
    def get_all_tags():
        return Tag.query.all()

    @staticmethod
    def get_tag_by_id(id):
        return Tag.query.get(id)

    @staticmethod
    def get_tags_by_name(name):
        return Tag.query.filter_by(name=name).all()
