#!/usr/bin/env python3
import sys

from setuptools import setup  # type: ignore

if sys.version_info < (3, 7, 0):
    sys.exit("Python 3.7 or later is required. ")

try:
    from flask import __version__ as flask_version  # type: ignore

    if flask_version < "2.0.0":
        sys.exit("Flask 2.x or later is required. ")
except ImportError:
    pass


requirements = [
    "Flask-SQLAlchemy>=2.5.1",
    "Flask-WTF>=1.0.0",
    "SQLAlchemy>=0.8.0",
    "asgiref>=3.2",
    "charset-normalizer[unicode_backport]>=2.0.12",
    "flask>=2.1.0",
    "python-dotenv>=0.20.0",
    "requests>=2.22.0",
]

docs_requirements = [
    "furo",
    "myst-parser",
    "sphinx-copybutton",
    "sphinx-design",
    "sphinx-inline-tabs",
    "sphinx-tabs",
]
dev_requirements = [
    "coverage",
    "flake8",
    "pre-commit",
    "pytest",
    "requests",
    *requirements,
    *docs_requirements,
]

setup(
    install_requires=requirements,
    extras_require={"dev": dev_requirements, "docs": docs_requirements},
    include_package_data=True,
    zip_safe=False,
)
