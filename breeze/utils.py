import random
from datetime import datetime
from hashlib import md5
from hashlib import sha3_512


def get_current_time():
    """Returns the current time in
    `UTC <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_.

    :return:
        :class:`datetime.datetime`
    """
    return datetime.utcnow()


def string_to_hash(string: str) -> str:
    """Converts a string to a hash.

    :args:
        ``string`` (`str`): input string

    :returns:
        `str`: hash of the string
    """
    return sha3_512(string.encode("utf-8")).hexdigest()


def check_password_hash(hash: bytes, password: str) -> bool:
    """Checks if a password matches a hash.

    :args:
        ``password`` (`str`): password to check
        ``hash`` (`bytes`): hash to check

    :returns:
        `bool`: True if the password matches the hash, False otherwise
    """
    if not password or not hash:
        return
    return sha3_512(password.encode("utf-8")).hexdigest() == hash


def get_image_from_gravatar(email: str) -> str:
    """Gets an image from gravatar.

    :args:
        ``email`` (`str`): email to get the image from gravatar

    :returns:
        `str`: url to the image
    """
    return "https://www.gravatar.com/avatar/" + md5(email.encode("utf-8")).hexdigest()


def get_random_string(length: int) -> str:
    """Generates a random string.

    :args:
        ``length`` (`int`): length of the string

    :returns:
        `str`: random string
    """
    letters = """abcdefghijklmnopqrstuvwxyz\
    ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\
    ~`!@#$%^&*()-_=+|}]{["':;?/>.<, """
    return "".join(random.choice(letters) for i in range(length))
