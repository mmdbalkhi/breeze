class BreezeException(Exception):
    """
    Base class for all Breeze exc.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PermissionError(BreezeException):
    """
    Exception raised when a user does not have permission to perform an action.
    """


class EmptyError(BreezeException):
    """
    Exception raised when a object is empty.
    """
