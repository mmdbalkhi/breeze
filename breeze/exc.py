class BreezeException(Exception):
    """Base class for all Breeze exceptions
    inherited from :class:`Exception`

    Attributes:
        :attr:`message` (str): the exception message
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PermissionError(BreezeException):
    """Exception raised when a user does not have permission to perform an action.
    inherited from :class:`breeze.exc.BreezeException`
    """


class EmptyError(BreezeException):
    """
    Exception raised when a object is empty.
    inherited from :class:`breeze.exc.BreezeException`
    """
