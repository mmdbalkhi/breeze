from datetime import datetime


def get_current_time() -> datetime.datetime:
    """
    Returns the current time in UTC.
    """
    return datetime.utcnow()
