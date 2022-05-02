from breeze import exc
from breeze import utils
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Users table on db

    inherited from :class:`flask_sqlalchemy.SQLAlchemy`

    :raises:
        :class:`breeze.exc.EmptyError`: if password is empty then raise this exception
        :class:`breeze.exc.PermissionError`: if user not have permission to perform
        an action then raise this exception

    Methods:
        :meth:`save`: save user to db
        :meth:`delete`: delete user from db
        :meth:`update`: update user from db

    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)  # len(sha512) == 128

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def save(self):
        """Save user to db

        :raises:
            :class:`breeze.exc.EmptyError`
        """
        if not self.password:
            raise exc.EmptyError("password is Empty")

        self.password = utils.string_to_hash(self.password)
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
        if not utils.check_password_hash(self.password, confirm_password):
            raise exc.PermissionError(message="Password is not correct")

        db.session.delete(user)
        db.session.commit()

    def update(self, title, content, confirm_password):
        """Update user from db

        :args:
            ``title`` (`str`): User profile title
            ``content`` (`str`): User profile info
            ``confirm_password`` (`hash`): User password to confirm delete
        """
        self.password = User.query.filter_by(email=self.email).first().password
        if confirm_password != self.password:
            raise exc.PermissionError(message="Password is not correct")

        self.title = title
        self.content = content
        db.session.commit()

    def check_password(self, password):
        """Check user password

        :args:
            ``password`` (`hash`): User password to confirm delete

        :return: `bool`: True if password is correct, False otherwise
        """
        return utils.check_password_hash(self.password, password)

    @staticmethod
    def get_all_users():
        return User.query.all()

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
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("posts", lazy=True))

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title, content):
        self.title = title
        self.content = content
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

    @staticmethod
    def get_posts_by_tag_id(tag_id):
        return Post.query.filter_by(tag_id=tag_id).all()

    @staticmethod
    def get_posts_by_title(title):
        return Post.query.filter_by(title=title).all()

    @staticmethod
    def get_comments_by_content(content):
        return Comment.query.filter_by(content=content).all()


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("comments", lazy=True))
    post = db.relationship("Post", backref=db.backref("comments", lazy=True))

    def __repr__(self):
        return f"Comment('{self.content}')"

        def save(self):
            db.session.add(self)

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, content):
        self.content = content
        db.session.commit()

    @staticmethod
    def get_all_comments():
        return Comment.query.all()

    @staticmethod
    def get_comment_by_id(id):
        return Comment.query.get(id)

    @staticmethod
    def get_comments_by_user_id(user_id):
        return Comment.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_comments_by_post_id(post_id):
        return Comment.query.filter_by(post_id=post_id).all()

    @staticmethod
    def get_comments_by_content(content):
        return Comment.query.filter_by(content=content).all()


class Tag(db.Model):
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
