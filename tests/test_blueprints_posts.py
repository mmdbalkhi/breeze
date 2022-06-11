from breeze.models import db
from breeze.models import Post
from breeze.models import User


def test_get_new_post(app, client):
    with app.app_context():
        # insure that the database is empty
        db.drop_all()
        db.create_all()

        # create a user
        user = User(
            username="test_new_post",
            email="test_new_post@test.com",
            password="test_new_post",
        )
        user.save()

        # login the user
        client.post(
            "/u/login", data={"username": "test_new_post", "password": "test_new_post"}
        )

    response = client.get("/p/new")
    client.get("/u/logout")
    assert response.status_code == 200


def test_new_post_redirect_if_not_login(client):
    respone = client.get("/p/new", follow_redirects=False)
    assert respone.status_code == 302


def test_new_post(app, client):
    with app.app_context():
        # insure that the database is empty
        db.drop_all()
        db.create_all()

        # create a user
        user = User(
            username="test_new_post",
            email="test_new_post@test.com",
            password="test_new_post",
        )
        user.save()

        # login the user
        client.post(
            "/u/login", data={"username": "test_new_post", "password": "test_new_post"}
        )

    response = client.post(
        "/p/new", data={"content": "test create a new post"}, follow_redirects=True
    )
    assert (
        response.status_code == 200
    )  # follow_redirects is True then it will redirect to the post page and get 200 status code
    assert b"Post created successfully." in response.data

    with app.app_context():
        # check that the post was created
        post = Post.query.first()
        assert post.content == "test create a new post"
        assert post.user_id == 1
        assert post.id == 1


def test_show_post(app, client):
    with app.app_context():
        # insure that the database is empty
        db.drop_all()
        db.create_all()

        # create a user
        user = User(
            username="test_new_post",
            email="test_new_post@test.com",
            password="test_new_post",
        )
        user.save()

        # login the user
        client.post(
            "/u/login", data={"username": "test_new_post", "password": "test_new_post"}
        )

        # create a post
        response = client.post(
            "/p/new", data={"content": "test create a new post"}, follow_redirects=True
        )

    response = client.get("/p/1")

    assert response.status_code == 200

    with app.app_context():
        # check that the post was created
        post = Post.query.first()
        assert post.content == "test create a new post"


def test_show_post_error(client):
    respone = client.get("/p/404")
    assert respone.status_code == 404


def test_delete_post(app, client):
    with app.app_context():
        # insure that the database is empty
        db.drop_all()
        db.create_all()

        # create a user
        user = User(
            username="test_delete_post",
            email="test_delete_post@test.com",
            password="test_delete_post",
        )
        user.save()
        client.post(
            "/u/login",
            data={"username": "test_delete_post", "password": "test_delete_post"},
        )

        # create a post
        client.post(
            "/p/new", data={"content": "test delete a post"}, follow_redirects=True
        )

    response = client.get("/p/1/delete")
    assert response.status_code == 302
    assert response.location == "/"


def test_delete_post_post_not_found(client):
    response = client.get("/p/404/delete")
    assert response.status_code == 404


def test_delete_post_not_login(app, client):
    with app.app_context():
        # insure that the database is empty
        db.drop_all()
        db.create_all()

        # create a user
        user = User(
            username="test_new_post",
            email="test@test.com",
            password="test_new_post",
        )
        user.save()
        client.post(
            "/u/login", data={"username": "test_new_post", "password": "test_new_post"}
        )
        client.post(
            "/p/new", data={"content": "test create a new post"}, follow_redirects=True
        )
        client.get("/u/logout")

    response = client.get("/p/1/delete")
    assert response.status_code == 302
    assert response.location == "/u/login"


def test_delete_post_not_auth(app, client):
    with app.app_context():
        # insure that the database is empty
        db.drop_all()
        db.create_all()

        # create a user
        user = User(
            username="test_new_post",
            email="test@test.com",
            password="test_new_post",
        )
        user.save()
        client.post(
            "/u/login", data={"username": "test_new_post", "password": "test_new_post"}
        )
        client.post(
            "/p/new", data={"content": "test create a new post"}, follow_redirects=True
        )
        client.get("/u/logout")

        user = User(
            username="test_new_post2",
            email="test2@test.com",
            password="test_new_post",
        )
        user.save()
        client.post(
            "/u/login", data={"username": "test_new_post2", "password": "test_new_post"}
        )

    response = client.get("/p/1/delete")

    assert response.status_code == 302
    assert response.location == "/p/1"
