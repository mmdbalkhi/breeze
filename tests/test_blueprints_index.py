from breeze import create_app

client = create_app().test_client()


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert b"breeze" in response.data
