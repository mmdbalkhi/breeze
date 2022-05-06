from pathlib import Path

from flask import Flask

from breeze import Config
from breeze import create_app


def test_create_app():
    assert isinstance(create_app(), Flask)


def test_create_app_if_db_is_exists():
    path = Path("breeze/breeze.db")
    path.touch()
    assert isinstance(create_app(), Flask)


def test_touch_dotenv():
    path = Path(Path.cwd() / ".env")
    path.write_text("SECRET_KEY='VERY_VERY_SECRET_KEY'")

    assert Config.dotenv_path == str(path)
