import pytest
from breeze import exc


def test_breeze_exception():
    with pytest.raises(exc.BreezeException):
        raise exc.BreezeException("Test")


def test_permission_error_exception():
    """Test this duplication and do not need this, but we test for coverage"""
    with pytest.raises(exc.PermissionError):
        raise exc.PermissionError("Test")


def test_empty_error_exception():
    """Test this duplication and do not need this, but we test for coverage"""
    with pytest.raises(exc.EmptyError):
        raise exc.EmptyError("Test")


def test_invalid_usage_exception():
    """Test this duplication and do not need this, but we test for coverage"""
    with pytest.raises(exc.InvalidUsage):
        raise exc.InvalidUsage("Test")
