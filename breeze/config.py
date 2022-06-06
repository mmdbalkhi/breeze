from os import environ

from breeze.utils import gen_random_string
from dotenv import find_dotenv
from dotenv import load_dotenv


class Config:
    """A base configuration class from which other configuration classes inherit.
    for use in :class:`flask.config.Config`
    """

    # load env vars from .env file if it exists
    if find_dotenv():  # pragma: no cover
        load_dotenv()

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = gen_random_string(128)
    SQLALCHEMY_DATABASE_URI = "sqlite:///breeze.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    ADMINS = [""]
    LOG_TO_STDOUT = False
    RECAPTCHA_PUBLIC_KEY = environ["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = environ["RECAPTCHA_PRIVATE_KEY"]
