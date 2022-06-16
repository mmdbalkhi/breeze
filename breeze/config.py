import logging
import sys
from os import environ

from breeze.utils import gen_random_string
from dotenv import find_dotenv
from dotenv import load_dotenv


class Config:
    """breeze configuration

    This class is used to store all the configuration variables.

    :attr:`DOMAIN`: The domain of the application.

    flask configs::
        :attr:`DEBUG`: A boolean value indicating whether the application is in debug mode or not.
        :attr:`TESTING`: A boolean value indicating whether the application is in testing mode or not.\n
        :attr:`SECRET_KEY`: A secret key for use in FLask(and flask extensions like flask-wtf).


    SQLAlchemy configs::
        :attr:`SQLALCHEMY_DATABASE_URI`: A string containing the URI of the database to use.\n
        :attr:`SQLALCHEMY_TRACK_MODIFICATIONS`: A boolean indicating whether or not to track modifications to the database.\n

    flask-wtf configs::
        :attr:`CSRF_ENABLED`: A boolean value indicating whether must use CSRF protection or not.\n
        :attr:`RECAPTCHA_PUBLIC_KEY`: A string containing the public key for use with Google's reCAPTCHA service.\n
        :attr:`RECAPTCHA_PRIVATE_KEY`: A string containing the private key for use with Google's reCAPTCHA service.

    oauth2 configs::
        :attr:`GITHUB_CLIENT_ID`: A string containing the client ID for use with GitHub's OAuth2 service.\n
        :attr:`GITHUB_CLIENT_SECRET`: A string containing the client secret for use with GitHub's OAuth2 service.\n
        :attr:`GITHUB_SCOPE`: A string containing the scope for use with GitHub's OAuth2 service.

        :attr:`DISCORD_CLIENT_ID`: A string containing the client ID for use with Discord's OAuth2 service.\n
        :attr:`DISCORD_CLIENT_SECRET`: A string containing the client secret for use with Discord's OAuth2 service.\n
        :attr:`DISCORD_SCOPE`: A string containing the scope for use with Discord's OAuth2 service.

    for more information on the configuration variables, see the documentation :doc:`/config` section.

    """

    logging.basicConfig(format="%(levelname)s: %(message)s")

    DOMAIN = environ.get("DOMAIN", "http://localhost:5000")

    DEBUG = False
    TESTING = False
    SECRET_KEY = gen_random_string(128)

    SQLALCHEMY_DATABASE_URI = "sqlite:///breeze.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CSRF_ENABLED = True

    # TODO: autogenerate .env file
    # load env vars from .env file if it exists
    if find_dotenv():  # pragma: no cover
        load_dotenv()

    # google recaptcha v2 api keys
    RECAPTCHA_PUBLIC_KEY = environ.get("RECAPTCHA_PUBLIC_KEY", "")
    RECAPTCHA_PRIVATE_KEY = environ.get("RECAPTCHA_PRIVATE_KEY", "")

    if not (RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY):  # pragma: no cover
        logging.error(
            "RECAPTCHA_PUBLIC_KEY and/or RECAPTCHA_PRIVATE_KEY not found in your .env file. "
            "please add them to your .env file and try again."
        )
        sys.exit(1)

    # oauth2 with github
    GITHUB_CLIENT_ID = environ.get("GITHUB_CLIENT_ID", "")
    GITHUB_CLIENT_SECRET = environ.get("GITHUB_CLIENT_SECRET", "")

    GITHUB_SCOPE = "user:email"  # we only need the user's email

    if not (GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET):  # pragma: no cover
        logging.warning(
            "if you want to use github oauth2, please set GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET in your .env file"
            " and try again. Otherwise, you can ignore this warning. ( if you don't want to use github oauth2 or this) "
            "testing will continue without github oauth2."
        )

    # oauth2 with discord
    DISCORD_CLIENT_ID = environ.get("DISCORD_CLIENT_ID", "")
    DISCORD_CLIENT_SECRET = environ.get("DISCORD_CLIENT_SECRET", "")

    # discord scope for get user name, email, and avatar
    DISCORD_SCOPE = "identify email"

    if not (DISCORD_CLIENT_ID and DISCORD_CLIENT_SECRET):  # pragma: no cover
        logging.warning(
            "if you want to use discord oauth2, please set DISCORD_CLIENT_ID and DISCORD_CLIENT_SECRET in your .env file"
            " and try again. Otherwise, you can ignore this warning. ( if you don't want to use discord oauth2 or this) "
            "testing will continue without discord oauth2."
        )
