from dataclasses import dataclass
from datetime import datetime
from typing import List

import requests

from pypocket.utils import convert_epoch_to_datetime


@dataclass
class PocketAPI:
    """Class for official GetPocket API endpoints"""

    get: str = "https://getpocket.com/v3/get"


@dataclass
class PocketArticle:
    """Class for official GetPocket API endpoints"""

    item_id: int
    title: str
    url: str
    tags: List[str]
    time_added: datetime
    time_updated: datetime


class Pocket(object):
    def __init__(self, consumer_key: str, access_token: str):
        self._consumer_key = consumer_key
        self._access_token = access_token
        self.pocket_endpoints = PocketAPI

    @staticmethod
    def _reformat_items(item):
        return PocketArticle(
            item_id=int(item["item_id"]),
            title=item["resolved_title"],
            url=item["resolved_url"],
            tags=[],
            time_added=convert_epoch_to_datetime(int(item["time_added"])),
            time_updated=convert_epoch_to_datetime(int(item["time_updated"])),
        )

    def retrieve(self, num_post: int = 5) -> List[PocketArticle]:
        """Retrieve saved articles

        Args:
            num_post (int):

        Returns:
            Dict

        """
        results = requests.get(
            url=self.pocket_endpoints.get,
            params={
                "consumer_key": self._consumer_key,
                "access_token": self._access_token,
                "count": str(num_post),
                "detailType": "complete",
            },
        )
        result_list = results.json()["list"]
        return [self._reformat_items(elem) for elem in result_list.values()]
