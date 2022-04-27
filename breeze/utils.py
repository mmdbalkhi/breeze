from datetime import datetime
from hashlib import sha3_512


def get_current_time():
    """Returns the current time in
    `UTC <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_.
    """
    return datetime.utcnow()


def string_to_bytes(string):
    """Converts a string to bytes.

    Args:
        ``string`` (`str`): input string

    Returns:
        `bytes`: _description_
    """
    return bytes(string, "utf-8")


def string_to_hash(string):
    """Returns the sha3_512 hash of a string.

    Args:
        ``string`` (`str`): input string

    Returns:
        `str`: sha3_512 hash of the string
    """
    return sha3_512(string_to_bytes(string)).hexdigest()


def check_password_hash(password, hash):
    """Checks if a password matches a hash.

    Args:
        ``password`` (`str`): password to check
        ``hash`` (`hash`): hash to check against

    Returns:
        bool: if password matches hash return True else False
    """
    return string_to_hash(password) == hash
