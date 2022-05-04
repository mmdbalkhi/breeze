import pytest
from breeze import utils


def test_get_current_time():
    assert utils.get_current_time() is not None
    assert 2022 <= utils.get_current_time().year <= 2030  # this code Valid until 2030
    assert 1 <= utils.get_current_time().month <= 12
    assert 1 <= utils.get_current_time().day <= 31


def test_string_to_bytes():
    assert isinstance(utils.string_to_bytes("test"), bytes)
    assert utils.string_to_bytes("test") == b"test"


def test_string_to_bytes_error():
    with pytest.raises(TypeError):
        utils.string_to_bytes(1)


def test_string_to_hash():
    assert isinstance(utils.string_to_hash("test"), bytes)
    assert utils.string_to_hash("test") != utils.string_to_hash("test2")


def test_check_password_hash():
    assert utils.check_password_hash("test", utils.string_to_hash("test"))
    assert not utils.check_password_hash("test2", utils.string_to_hash("test"))
