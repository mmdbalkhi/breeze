from breeze.models import Post
from breeze.models import User
from breeze.utils import get_current_time


def test_create_comment_not_found(client):
    res = client.get("/p/404/new")
    assert res.status_code == 404


def test_create_comment(app, client):
    with app.app_context():
        user = User(
            username="test_create_comment",
            email="test_create_comment@test.com",
            password="test_create_comment",
        )
        user.save()

        client.post(
            "/u/login",
            data={"username": "test_create_comment", "password": "test_create_comment"},
        )

        post = Post(user=user, content="test1", time=get_current_time())
        post.save()

    res = client.post("/p/1/new", data={"content": "test comment"})
    assert res.status_code == 302
    assert res.location == "/p/1"


def test_get_create_comment_page(client):
    client.post(
        "/u/login",
        data={"username": "test_create_comment", "password": "test_create_comment"},
    )
    res = client.get("/p/1/new")
    assert res.status_code == 200


def test_create_comment_not_login(client):
    client.get("/u/logout")

    res = client.get("/p/1/new")

    assert res.status_code == 302
    assert res.location == "/u/login"
