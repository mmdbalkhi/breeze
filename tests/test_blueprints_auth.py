from breeze import create_app

client = create_app().test_client()


def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Breeze!" in response.data


def test_register_get():
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data


def test_register_400_error():
    response = client.post(
        "/register", data=dict(username="testregister"), follow_redirects=True
    )
    assert response.status_code == 400
    response = client.post(
        "/register", data=dict(email="testregister@test.com"), follow_redirects=True
    )
    assert response.status_code == 400
    response = client.post(
        "/register", data=dict(password="testregister"), follow_redirects=True
    )
    assert response.status_code == 400

    assert b"please fill out all fields" in response.data


def test_get_login():
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data


def test_400_error_login():
    response = client.post(
        "/login", data=dict(username="testregister"), follow_redirects=True
    )
    assert response.status_code == 400
    response = client.post(
        "/login", data=dict(password="testregister"), follow_redirects=True
    )
    assert response.status_code == 400

    assert b"Username and password are required." in response.data


def test_logout():
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"You have been logged out." in response.data
