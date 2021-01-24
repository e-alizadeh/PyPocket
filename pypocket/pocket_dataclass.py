from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class PocketItem:
    """Class for details of each Pocket item"""

    item_id: int
    title: str
    url: str
    tags: List[str]
    time_added: datetime
    time_updated: datetime

    @staticmethod
    def convert_datetime_to_string(dt: datetime) -> str:
        """Convert datetime into a human readable date string
        Get the date (in UTC)

        Args:
            dt (datetime):

        Returns:
            Date (str):
        """
        return dt.strftime("%a, %d %b %Y")
