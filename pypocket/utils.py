import time
from datetime import datetime


def convert_epoch_to_utc_datetime(epoch: int) -> datetime:
    return datetime.utcfromtimestamp(epoch)


def convert_epoch_to_human_readable_date(epoch: int) -> str:
    """Convert epoch timestamp into a human readable date
    Get the date (in UTC)

    Args:
        epoch (int):

    Returns:
        Date(str):
    """
    dt = convert_epoch_to_utc_datetime(epoch)
    return dt.strftime("%a, %d %b %Y")
