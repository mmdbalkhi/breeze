class BreezeException(Exception):
    """
    Base class for all Breeze exceptions.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
