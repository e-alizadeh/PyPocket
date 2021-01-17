from dataclasses import dataclass
from datetime import datetime
from typing import List

import requests


@dataclass
class PocketAPI:
    """Class for official GetPocket API endpoints"""

    get: str = "https://getpocket.com/v3/get"


@dataclass
class PocketArticle:
    """Class for official GetPocket API endpoints"""

    title: str
    url: str
    tags: List[str]
    timestamp: datetime


class Pocket(object):
    def __init__(self, consumer_key: str, access_token: str):
        self._consumer_key = consumer_key
        self._access_token = access_token
        self.pocket_endpoints = PocketAPI

    def retrieve(self, num_post: int = 5):
        """Retrieve saved articles

        Args:
            num_post (int):

        Returns:
            Dict

        """
        result = requests.get(
            url=self.pocket_endpoints.get,
            params={
                "consumer_key": self._consumer_key,
                "access_token": self._access_token,
                "count": str(num_post),
                "detailType": "complete",
            },
        )
        return result
