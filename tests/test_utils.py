import pytest
import requests
from breeze import utils


def test_get_current_time():
    assert utils.get_current_time() is not None
    assert 2022 <= utils.get_current_time().year <= 2030  # this code Valid until 2030
    assert 1 <= utils.get_current_time().month <= 12
    assert 1 <= utils.get_current_time().day <= 31


def test_string_to_bytes():
    assert isinstance(utils.string_to_bytes("test"), bytes)
    assert utils.string_to_bytes("test") == b"test"
    assert isinstance(utils.string_to_bytes(b"test"), bytes)
    assert utils.string_to_bytes(b"test") == b"test"


def test_string_to_bytes_error():
    with pytest.raises(TypeError):
        utils.string_to_bytes(1)


def test_string_to_hash():
    assert isinstance(utils.string_to_hash("test"), str)
    assert utils.string_to_hash("test") != utils.string_to_hash("test2")
    assert utils.string_to_hash("test") != "test"
    assert (
        utils.string_to_hash("very secret password")
        == "6e43ad2674c6a092d8a117958b4449fa2f28b01b3e26a120e8cca17ef0326c3d9bb951d3339fef7d100c4c6448bc00d0a1b7c4c0945334d143ff6991248e7d26"  # noqa: B950
    )


def test_check_password_hash():
    assert utils.check_password_hash(
        utils.string_to_hash("test"),
        "test",
    )
    assert not utils.check_password_hash(
        utils.string_to_hash("test"),
        "test2",
    )
    assert not utils.check_password_hash(None, "hash")
    assert not utils.check_password_hash("password", None)


def test_get_image_from_gravatar():
    assert isinstance(utils.get_image_from_gravatar("user@test.com"), str)
    assert (
        requests.get(utils.get_image_from_gravatar("user@test.com")).status_code == 200
    )
