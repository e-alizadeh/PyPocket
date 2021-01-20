import time
from datetime import datetime


def convert_epoch_to_datetime(epoch: int) -> datetime:
    return datetime.fromtimestamp(epoch)


def convert_epoch_to_human_readable_datetime(epoch: int) -> str:
    """Convert epoch timestamp into human readable time

    Args:
        epoch (int):

    Returns:
        str: Date and time including the day and timezone
    """
    return time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
