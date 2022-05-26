import random
import re
from datetime import datetime
from hashlib import md5
from hashlib import sha3_512
from typing import Union

from charset_normalizer import from_bytes


def get_current_time() -> datetime:
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


def check_hash(hash: bytes, password: str) -> Union[bool, None]:
    """Checks if a password matches a hash.

    :args:
        ``password`` (`str`): password to check
        ``hash`` (`bytes`): hash to check

    :returns:
        `bool`: True if the password matches the hash, False otherwise
    """
    if not password or not hash:
        return None

    return sha3_512(password.encode("utf-8")).hexdigest() == hash


def get_image_from_gravatar(email: str) -> str:
    """Gets an image from gravatar.

    first, this function Generate md5 of the user's email and next
    returned this hash with gravatar URL

    if this URL is not found(404) gravatar shows the default avatar
    else show self users avatar from gravatar

    :args:
        ``email`` (`str`): email to get the image from gravatar

    :returns:
        `str`: url to the image
    """
    email_md5 = md5(email.encode("utf-8")).hexdigest()
    return f"https://www.gravatar.com/avatar/{email_md5}"


def gen_random_string(length: int) -> str:
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


def normalise(string: Union[str, bytes, None]) -> str:
    """Normalise a string.

    :args:
        ``string`` (`str`): input string

    :returns:
        `str`: normalised string
    """
    if not string:
        return ""
    if isinstance(string, str):
        string = string.encode("utf-8")
    string = str(from_bytes(string).best())
    return string.lower().strip()


def normalise_email(email: Union[str, None]) -> Union[str, bool]:
    """check and normalise user emails

    **pattern:**

    a regex pattern to check for normalised email,

    part of the *pattern* is the email domain:

    1. username(`*username*@domain.ex`)
        can be digested or litter::
            `breeze1234`

    2. domain(`username@*domain*.ex`)
        can be only litters::
            `email`

    3. extension(`username@domain.*extension*`)
        can only litter with 2, 3 or 4 length::
            `com` or `io` or `wiki`

    if the user's email matches the pattern return email

    :args:
        ``email`` (`str`): input email

    :returns:
        `str`: normalized email
        `bool`: flase if email is invalid or None
    """

    email = normalise(email)

    if not email:
        return False

    email_split_ = email.split("@")
    if not len(email_split_) == 2:
        return False

    pattern = r"^[a-z0-9]+@+[a-z]+\.+[a-z]{2,3}$"  # all domains lenght is 2 or 3
    if re.match(pattern, email):
        return email

    username, domain = email_split_  # username, email.com
    del email_split_

    username = re.sub(
        r"(\.)*(\+.*)*", "", username
    )  # remove *.* and *+(in many email service +tag add tag to email)*

    if not re.match(r"^[a-z]+\.+[a-z]{2,4}$", domain):
        return False

    if not re.match(r"^[a-z0-9]+", username):
        return False

    return f"{username}@{domain}"
