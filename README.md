<p algin="center">
    <img src="https://raw.githubusercontent.com/mmdbalkhi/breeze/main/artwork/breeze.png">
</p>

<h5 align="center"> a flask application similar to Twitter just For Fun!</h5>

<p align="center">
    <a href="https://github.com/mmdbalkhi/breeze/tree/main/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg">
    </a>
    <a href='https://python-breeze.readthedocs.io/?badge=latest'>
        <img src='https://readthedocs.org/projects/python-breeze/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://github.com/mmdbalkhi/breeze/actions/workflows/tests.yaml">
        <img src="https://github.com/mmdbalkhi/breeze/actions/workflows/tests.yaml/badge.svg"
        alt="test badge">
    </a>
    <a href="https://codecov.io/gh/mmdbalkhi/breeze">
        <img src="https://codecov.io/gh/mmdbalkhi/breeze/branch/main/graph/badge.svg?token=6C8nLeyYht"/>
    </a>
</p>

the breeze is a fun web application for practising with [Flask](https://flask.palletsprojects.com/), [SQLalchemy](https://www.sqlalchemy.org/) and a few other things that try to be similar to **Twitter**!

## Run the breeze

* breeze need to [python](https://python.org) 3.7 or upper

first your need to install breeze requirements:

```bash
pip install -e .
```

then your add breeze to your environment and run breeze:

* bash:

```bash
export FLASK_APP=breeze
flask run
```

* fish

```fish
set -x FLASK_APP breeze
flask run
```

* cmd

```
set FLASK_APP=breeze
flask run
```

* powershell

```
$env:FLASK_APP = "breeze"
flask run
```

now you can visit your breeze on your browser: [http://localhost:5000/](http://localhost:5000/)

## TODOs

this section is breeze todos. we use this section to keep track of all the todos in breeze.

* **tags**:

we use tags to categorize todos. on the future, maybe we will use tools to help you to categorize todos but for now, you can just add custom tags to your todos.

* ~[async]: todos that are related to async programming.~
* [auth]: authentication related like login, logout, register, etc.
* [db]: database related like migration, seeding, etc.
* [frontend]: frontend related like jinja2, pages, etc.
* [mention]: like twitter mention
* [notification]: notification related like notification sys, etc.
* [post]: post(or comment) related like post, post edit, etc.
* [profile]: profile related like profile, profile edit, etc.
* [search]: search related like search engine, etc.
* [utils]: utils related like check time, etc.

> **__issues__** after review may be add to here.

* [x] add user authentication
    - [ ] auth with other services like Google, GitHub, Twitter, etc.[auth]
    - [ ] user can change their data like password, email, etc.[setting]
    - [ ] user can delete their data[setting]
    - [X] add check for duplicate username, email, etc.[db]
    - [ ] add verification for emails with link, send code, etc.[auth]
    - [ ] use Captcha for verification like reCaptcha, etc.[auth]
* [x] add user profile
    - [X] support [gravatar](https://en.gravatar.com/)[profile]
    - [ ] support cutsom avatar[profile][setting]
    - [ ] support custom background[profile][setting]
    - [ ] user can edit their profile and add their bio and info[profile]
        - [ ] bio: short description about yourself[profile]
        - [ ] info: many datas like location, birthday, etc.[profile]
* [X] create a post or comment[post]
    - [ ] delete post or comment[post]
    - [ ] like post or comment[post][db]
    - [ ] edit post or comment[post]
        - [ ] time limit for edit[post][utils]
    - [ ] retweet post or comment[post]
        - [ ] add description for retweet[post]
    - [X] add comment for post[post]
    - [ ] add comment for comment[post]
    - [ ] mention user in post or comment[post][mention]
* [ ] ~use `Asynchronous` in project[async]~
    > ~for more information, please visit [flask docs](https://flask.palletsprojects.com/en/2.1.x/async-await/) (new in 2.x version)~
    why this won't do? because flask for now is not support async fully.(see issue [#13](https://github.com/mmdbalkhi/breeze/issues/13))

* [ ] tag system
    - [ ] add tag for post or comment[post]
    - [ ] add tag for user bio[profile]
    - [ ] search posts(or other things) by tag[post][tag][search]
* [ ] add a search system[search]
    - [ ] use tag system for search[search]
    - [ ] search by username[search]
    - [ ] search by text[search]
    > we can use [algolia](https://www.algolia.com/) or [elasticsearch](https://www.elastic.co/) but if we use flask, we need to use wtf-forms to handle the form.

* [ ] add a notification system[notification]
    - [ ] user can allow or disallow notifications for a post(or other things)[notification]
    > when user like a post or comment, we can send a notification to the user who post or comment the post or comment.

* [ ] add a message system(like twitter DM)[message]
    - [ ] user can send a message to another user[message]
    - [ ] ban and onban user[message][auth]
    - [ ] user can delete/edit their message[message]

* **frontend**:

> I'm not sure if we need to use [react](https://reactjs.org/) or [vue](https://vuejs.org/) for frontend. we can use pure flask and bootstrap for frontend. of course, we can use [flask-admin](https://flask-admin.readthedocs.io/en/latest/) for admin panel...

* [ ] fix post and comment form[frontend]
    - [ ] fix post form[frontend]
    - [ ] fix comment form[frontend]
    - bootstrap or other css framework
* [ ] fix user profile[frontend]
    - [ ] use bootstrap and other css framework(if need) for improve user profile page[frontend]
* [ ] fix auth page[frontend]

* **docs and api**:

* [X] add docs for api[docs]
* [ ] fix problem on show TOODs on the documention page[docs]
