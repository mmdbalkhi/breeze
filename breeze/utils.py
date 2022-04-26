from datetime import datetime
from hashlib import sha3_512


def get_current_time():
    """
    Returns the current time in UTC.
    """
    return datetime.utcnow()


def string_to_bytes(string):
    """
    Converts a string to bytes.
    """
    return bytes(string, "utf-8")


def string_to_hash(string):
    """
    Returns the sha3_512 hash of a string.
    """
    return sha3_512(string_to_bytes(string)).hexdigest()


def check_password_hash(password, hash):
    """
    Checks if a password matches a hash.
    """
    return string_to_hash(password) == hash
