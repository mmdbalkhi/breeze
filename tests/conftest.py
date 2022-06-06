import pytest
from breeze import create_app


@pytest.fixture
def app():
    return create_app({"TESTING": True})


@pytest.fixture
def client():
    app = create_app({"TESTING": True})

    return app.test_client()
