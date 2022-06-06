# TODOs

this file is breeze todos file. we use this file to keep track of all the todos in breeze.

## tags

we use tags to categorize todos. on the future, maybe we will use tools to help you to categorize todos but for now, you can just add custom tags to your todos.

* [async]: todos that are related to async programming.
* [auth]: authentication related like login, logout, register, etc.
* [db]: database related like migration, seeding, etc.
* [frontend]: frontend related like jinja2, pages, etc.
* [mention]: like twitter mention
* [notification]: notification related like notification sys, etc.
* [post]: post(or comment) related like post, post edit, etc.
* [profile]: profile related like profile, profile edit, etc.
* [search]: search related like search engine, etc.
* [utils]: utils related like check time, etc.

## TODO

**issues** after review may be add to here.

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
* [ ] use `Asynchronous` in project[async]
    > for more information, please visit [flask docs](https://flask.palletsprojects.com/en/2.1.x/async-await/) (new in 2.x version)

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

## frontend

I'm not sure if we need to use [react](https://reactjs.org/) or [vue](https://vuejs.org/) for frontend. we can use pure flask and bootstrap for frontend. of course, we can use [flask-admin](https://flask-admin.readthedocs.io/en/latest/) for admin panel...

* [ ] fix post and comment form[frontend]
    - [ ] fix post form[frontend]
    - [ ] fix comment form[frontend]
    - bootstrap or other css framework
* [ ] fix user profile[frontend]
    - [ ] use bootstrap and other css framework(if need) for improve user profile page[frontend]
* [ ] fix auth page[frontend]

## docs and api

* [X] add docs for api[docs]
* [ ] fix problem on show TOODs on the documention page[docs]
