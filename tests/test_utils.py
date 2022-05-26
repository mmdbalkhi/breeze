import pytest
import requests
from breeze import utils


def test_get_current_time():
    assert utils.get_current_time() is not None
    assert 2022 <= utils.get_current_time().year <= 2030  # this code Valid until 2030
    assert 1 <= utils.get_current_time().month <= 12
    assert 1 <= utils.get_current_time().day <= 31


def test_string_to_hash():
    assert isinstance(utils.string_to_hash("test"), str)
    assert utils.string_to_hash("test") != utils.string_to_hash("test2")
    assert utils.string_to_hash("test") != "test"
    assert (
        utils.string_to_hash("very secret password")
        == "6e43ad2674c6a092d8a117958b4449fa2f28b01b3e26a120e8cca17ef0326c3d9bb951d3339fef7d100c4c6448bc00d0a1b7c4c0945334d143ff6991248e7d26"  # noqa: B950
    )


def test_check_hash():
    assert utils.check_hash(
        utils.string_to_hash("test"),
        "test",
    )
    assert not utils.check_hash(
        utils.string_to_hash("test"),
        "test2",
    )
    assert not utils.check_hash(None, "hash")
    assert not utils.check_hash("password", None)


def test_get_image_from_gravatar():
    assert isinstance(utils.get_image_from_gravatar("user@test.com"), str)

    try:
        assert (
            requests.get(
                utils.get_image_from_gravatar("user@test.com"), timeout=1
            ).status_code
            == 200
        )
    except requests.exceptions.ConnectionError:  # pragma: no cover
        pytest.skip("internet connection is not available")


def test_gen_random_string():
    assert isinstance(utils.gen_random_string(10), str)
    assert len(utils.gen_random_string(10)) == 10


@pytest.mark.parametrize("case", ["test", "تست", "prueba", "テスト", "测试"])
def test_normalise(case):
    assert utils.normalise(case) == case


@pytest.mark.parametrize("case", [b"byte", "str", b"str", None])
def test_normalise_types(case):
    assert isinstance(utils.normalise(case), str)


@pytest.mark.parametrize(
    "case0",
    [
        "test@test.com",
        "test.test@test.io",
        "test.test+test@test.wiki",
        "test.com",
        "test@test",
        "ایمیل@test.com",
        "",
    ],
)
def test_normalise_email_type(case0):
    assert utils.normalise_email(case0) in [
        "test@test.com",
        "testtest@test.io",
        "testtest@test.wiki",
        False,
    ]
