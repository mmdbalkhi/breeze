from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    """Register form. this is the form that is used to register a new user."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Repeat Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """Login form. this is the form that is used to login to the website."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    recaptcha = RecaptchaField()
    submit = SubmitField("Sign In")


class PostForm(FlaskForm):
    """Post form. this is the form that is used to create a new post.
    this class can be use to create a new comment as well.
    """

    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")
