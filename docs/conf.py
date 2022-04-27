# -- Location of breeze ------------------------------------------------------
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "breeze"
copyright = "2022, Komeil Parseh"
author = "Komeil Parseh"


# -- General configuration ---------------------------------------------------

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]

autodoc_typehints = "description"
issues_github_path = "mmdbalkhi/breeze"

# -- Options for Markdown files ----------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# -- HTML configuration ---------------------------------------------------

html_theme = "furo"
html_logo = "../artwork/breeze.png"

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/mmdbalkhi/breeze",
            "html": "",
            "class": "fa-solid fa-github fa-2x",
        },
    ],
}

html_static_path = ["_static"]
