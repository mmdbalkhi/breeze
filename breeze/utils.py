from datetime import datetime
from hashlib import sha3_512


def get_current_time():
    """Returns the current time in
    `UTC <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_.

    :return:
        :class:`datetime.datetime`
    """
    return datetime.utcnow()


def string_to_bytes(string):
    """Converts a string to bytes.

    :args:
        ``string`` (`str`): input string

    :return:
        `bytes`: _description_
    """
    return bytes(string, "utf-8")


def string_to_hash(string):
    """Returns the sha3_512 hash of a string.

    :args:
        ``string`` (`str`): input string

    :return:
        `str`: sha3_512 hash of the string
    """
    return sha3_512(string_to_bytes(string)).hexdigest()


def check_password_hash(hash, password):
    """Checks if a password matches a hash.

    :args:
        ``password`` (`str`): password to check
        ``hash`` (`hash`): hash to check against

    :return:
        `bool`: if password matches hash return True else False
    """
    return hash == string_to_hash(password)
