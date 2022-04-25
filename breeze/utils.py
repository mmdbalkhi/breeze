from datetime import datetime


def get_current_time():
    """
    Returns the current time in UTC.
    """
    return datetime.utcnow()
