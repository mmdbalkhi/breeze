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
    # flake8: noqa B950
    assert isinstance(utils.string_to_hash("test"), str)
    assert (
        utils.string_to_hash("test")
        == "9ece086e9bac491fac5c1d1046ca11d737b92a2b2ebd93f005d7b710110c0a678288166e7fbe796883a4f2e9b3ca9f484f521d0ce464345cc1aec96779149c14"
    )
    assert (
        utils.string_to_hash("very secret password")
        == "6e43ad2674c6a092d8a117958b4449fa2f28b01b3e26a120e8cca17ef0326c3d9bb951d3339fef7d100c4c6448bc00d0a1b7c4c0945334d143ff6991248e7d26"
    )


def test_check_password_hash():
    assert utils.check_password_hash(
        "very secret password",
        "6e43ad2674c6a092d8a117958b4449fa2f28b01b3e26a120e8cca17ef0326c3d9bb951d3339fef7d100c4c6448bc00d0a1b7c4c0945334d143ff6991248e7d26",
    )
    assert not utils.check_password_hash("nice password", "this is hash?")
