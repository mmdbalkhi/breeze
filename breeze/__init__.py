""" a flask application similar to Twitter just for fun!
"""

from breeze.auth import Auth
from breeze.blueprints import auth_bp, blog_bp, home_bp, user_bp
from breeze.commands import create_admin, create_db, drop_db
from breeze.config import Config
from breeze.create_app import create_app
from breeze.database import db
from breeze.errors import InternalServerError, PageNotFound
from breeze.exceptions import BreezeException
# from breeze.extensions import cache, csrf, login_manager, mail, migrate
from breeze.models import Comment, Post, Tag, User
from breeze.utils import get_current_time


class BreezeConfig(Config):
    """load env variables from .env file"""

    dotenv_path = find_dotenv()
    if not dotenv_path:
        raise FileExistsError(f"{dotenv_path} not exists.")
    load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY")