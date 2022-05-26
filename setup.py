#!/usr/bin/env python3
import sys

from setuptools import setup  # type: ignore

if sys.version_info < (3, 7, 0):
    sys.exit("Python 3.7 or later is required. ")

requirements = [
    "flask>=2.1.0",
    "python-dotenv>=0.20.0",
    "SQLAlchemy>=0.8.0",
    "Flask-SQLAlchemy>=2.5.1",
    "charset-normalizer[unicode_backport]>=2.0.12",
    "python-dotenv>=0.20.0",
]
docs_requirements = [
    "furo",
    "myst-parser",
    "sphinx-copybutton",
    "sphinx-design",
    "sphinx-inline-tabs",
    "sphinx-tabs",
]
dev_requirements = ["pytest", *requirements, *docs_requirements]

setup(
    install_requires=requirements,
    extras_require={"dev": dev_requirements, "docs": docs_requirements},
    include_package_data=True,
    zip_safe=False,
)
