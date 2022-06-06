# contributing to the project

this project is open source, and we welcome contributions from the community in any way.
your contributions will be reviewed by a team member and will be integrated into the project as soon as possible.

## support questions

please don't hesitate to ask questions, and we will try to answer them as soon as possible. your can ask questions in the [github-discussion](https://github.com/mmdbalkhi/breeze/discussions) Please don't use the issue tracker for this. The issue tracker is a tool to address bugs and feature requests in Breeze itself.

## Reporting issues

Include the following information when reporting issues:

* Describe what you expected to happen.
* Describe what you actually did.
* List your Python, Flask and SQLalchemy version, OS, and other relevant details.

## Submitting pull requests

your can work on any issue without assigning it to a member. if your like work on a feature, you can see [TODO.md](TODO.md) for find TODOs. but if you like to work on a bug, you can report bug in the [issue tracker](https://github.com/mmdbalkhi/breeze/issues) and work on it.

Include the following in your patch:

* use [black](https://black.readthedocs.io/en/stable/) to format your code.  This and other tools will run automatically if you install [pre-commit](https://pre-commit.com/) using the instructions below.
* Include tests if your patch adds or changes code. Make sure the test fails without your patch.
* Update any relevant docs pages and docstrings. Docs pages and docstrings should be wrapped at 72 characters.

### work on a feature or fix a bug

steps:

* 1: [fork](https://github.com/mmdbalkhi/breeze/fork) the project and clone the repo.
* 2: Clone the main repository locally.

```bash
git clone https://github.com/mmdbalkhi/breeze
cd breeze
```

* 3: Add your fork as a remote to push your work to. Replace {username} with your username. This names the remote "fork", the default Pallets remote is "origin".

```bash
git remote add fork https://github.com/{username}/breeze
```

* 4: install and set-up virtualenv.
     - *nix

```bash
     python3 -m venv env
     . env/bin/activate
```

     - windows

```
     > py -3 -m venv env
     > env\Scripts\activate
```

* 4.2: Upgrade pip and setuptools.

```bash
     pip install --upgrade pip setuptools
```

* 4.3: Install the dependencies, then install breeze in editable mode.

```bash
pip install -r requirements.txt && pip install -e .
```

* 4.4: install pre-commit hooks

```bash
pip install pre-commit
pre-commit install
```

* 5: [create a branch](https://help.github.com/en/articles/using-branches-tags-and-labels-in-github-pull-requests)

```bash
git fetch origin
git checkout -b your-branch-name origin/main
```

* 6: Using your favorite editor, make your changes, committing as you go.

* 6.2 Include tests that cover any code changes you make. Make sure the test fails without your patch. Run the tests as described below.

* 6.3 Push your commits to your fork on GitHub and create a pull request. Link to the issue being addressed with fixes #123 in the pull request.

```bash
$ git push --set-upstream fork your-branch-name
```

* 7: Run the tests.

```bash
pytest
```

* 7.2: Running test coverage

Generating a report of lines that do not have test coverage can indicate where to start contributing. Run `pytest` using `coverage` and generate a report.

```bash
pip install coverage
coverage run -m pytest
coverage html
```

Open `htmlcov/index.html` in your browser to explore the report.

Read more about [coverage](https://coverage.readthedocs.io/en/latest/index.html) and [pytest](https://docs.pytest.org/en/latest/usage.html#usage).

#### Building the docs

Build the docs in the docs directory using `Sphinx` .

```bash
cd docs
make html
```

Open `_build/html/index.html` in your browser to view the docs.

Read more about [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html).
