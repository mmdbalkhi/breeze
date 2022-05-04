from datetime import datetime

import bcrypt


def get_current_time():
    """Returns the current time in
    `UTC <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_.

    :return:
        :class:`datetime.datetime`
    """
    return datetime.utcnow()


def string_to_bytes(string: str) -> bytes:
    """Converts a string to bytes.

    :args:
        ``string`` (`str`): String to convert
    :return:
        `bytes` : Converted string
    """
    return bytes(string, "utf-8")


def string_to_hash(string: str) -> bytes:
    """Converts a string to a hash.

    :args:
        ``string`` (`str`): input string

    :returns:
        `bytes`: hash of the string
    """
    return bcrypt.hashpw(string_to_bytes(string), bcrypt.gensalt())


def check_password_hash(password: str, hash: bytes) -> bool:
    """Checks if a password matches a hash.

    :args:
        ``password`` (`str`): password to check
        ``hash`` (`bytes`): hash to check

    :returns:
        `bool`: True if the password matches the hash, False otherwise
    """
    if not (password or hash):
        return
    return bcrypt.checkpw(string_to_bytes(password), hash)
