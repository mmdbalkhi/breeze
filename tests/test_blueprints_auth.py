from breeze import create_app
from breeze.models import db
from breeze.models import User

app = create_app()
client = create_app().test_client()


def test_register_get():
    response = client.get("/u/register")
    assert response.status_code == 200
    assert b"Register" in response.data


def test_register_user():
    response = client.post(
        "/u/register",
        data=dict(
            username="testregister", email="testregister@test.com", password="1234"
        ),
    )
    assert response.status_code == 302  # redirect to login page after register
    assert response.location == "/u/login"


def test_register_400_error():
    response = client.post(
        "/u/register", data=dict(username="testregister"), follow_redirects=True
    )
    assert response.status_code == 400
    response = client.post(
        "/u/register", data=dict(email="testregister@test.com"), follow_redirects=True
    )
    assert response.status_code == 400
    response = client.post(
        "/u/register", data=dict(password="testregister"), follow_redirects=True
    )
    assert response.status_code == 400

    assert b"please fill out all fields" in response.data


def test_user_is_exist():
    with app.app_context():
        # Ensures that the database is emptied for next unit test
        db.drop_all()

        db.create_all()
        user = User(
            username="testUserIsExist",
            email="testUserIsExist@test.com",
            password="testUserIsExist",
        )
        user.save()
    response = client.post(
        "/u/register",
        data=dict(
            username="testUserIsExist",
            email="testUserIsExist@test.com",
            password="testUserIsExist",
        ),
    )
    assert response.status_code == 400
    assert b"User testUserIsExist is already registered." in response.data


def test_get_login():
    response = client.get("/u/login")
    assert response.status_code == 200
    assert b"Login" in response.data


def test_400_error_login():
    response = client.post(
        "/u/login", data=dict(username="testregister"), follow_redirects=True
    )
    assert response.status_code == 400
    response = client.post(
        "/u/login", data=dict(password="testregister"), follow_redirects=True
    )
    assert response.status_code == 400

    assert b"Username and password are required." in response.data


def test_login_user():
    with app.app_context():
        # Ensures that the database is emptied for next unit test
        db.drop_all()

        db.create_all()
        user = User(
            username="testLoginUser",
            email="testLoginUser@test.com",
            password="1234",
        )
        user.save()
    response = client.post(
        "/u/login",
        data=dict(
            username="testLoginUser",
            password="1234",
        ),
    )
    assert response.status_code == 302  # redirect to profile page after login
    assert response.location == "/u/profile"


def test_incorrect_username_or_password():
    with app.app_context():
        # Ensures that the database is emptied for next unit test
        db.drop_all()

        db.create_all()
        user = User(
            username="testLoginUser",
            email="testLoginUser@test.com",
            password="1234",
        )
        user.save()

    response = client.post(
        "/u/login",
        data=dict(
            username="testincorrectLoginUser",
            password="1234",
        ),
    )
    assert response.status_code == 401
    assert b"Incorrect username or password." in response.data

    response = client.post(
        "/u/login",
        data=dict(
            username="testLoginUser",
            password="incorrectpassword",
        ),
    )
    assert response.status_code == 401
    assert b"Incorrect username or password." in response.data


def test_logout():
    response = client.get("/u/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"You have been logged out." in response.data


def test_user_page():
    with app.app_context():
        # Ensures that the database is emptied for next unit test
        db.drop_all()

        db.create_all()
        user = User(
            username="testUserPage", email="testUserPage@test.com", password="12345678"
        )
        user.save()
    response = client.get("/u/testUserPage", follow_redirects=True)
    assert response.status_code == 200
    assert b"testUserPage" in response.data


def test_user_page_error():
    response = client.get("/u/404User", follow_redirects=True)
    assert response.status_code == 404


def test_profile():
    with app.app_context():
        # Ensures that the database is emptied for next unit test
        db.drop_all()

        db.create_all()
        user = User(
            username="testProfile",
            email="testProfile@test.com",
            password="1234",
        )
        user.save()

    # login user
    response = client.post(
        "/u/login",
        data=dict(
            username="testProfile",
            password="1234",
        ),
    )

    response = client.get("/u/profile", follow_redirects=False)
    assert response.status_code == 302  # redirect to /u/profile
    assert response.location == "/u/testProfile"

    response = client.get("/u/profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"testProfile" in response.data


def test_profile_error():
    with app.app_context():
        # Ensures that the database is emptied for next unit test
        db.drop_all()

        db.create_all()

    # logout user
    client.get("/u/logout", follow_redirects=False)

    response = client.get("/u/profile", follow_redirects=False)

    assert response.status_code == 302  # redirect to login page
    assert response.location == "/u/login"

    response = client.get("/u/profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"you must be logged in to see your profile" in response.data
