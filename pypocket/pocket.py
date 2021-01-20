from dataclasses import dataclass
from datetime import datetime
from typing import List

import pandas as pd
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
    def __init__(
        self, consumer_key: str, access_token: str, html_filename: str = "report"
    ):
        self._consumer_key = consumer_key
        self._access_token = access_token
        self.pocket_endpoints = PocketAPI

        # Handle both scenarios where the html_filename has either .html extension or not.
        self.html_output_filename = (
            html_filename
            if html_filename.endswith(".html")
            else f"{html_filename}.html"
        )

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

    def to_html(self):
        results_df = pd.DataFrame(data=self.retrieve())
        with open(f"./{self.html_output_filename}", "w", encoding="utf-8") as f:
            f.write(
                results_df.to_html(render_links=True, justify="center").replace(
                    '<table border="1" class="dataframe">',
                    '<table class="table table-striped">',
                )  # use bootstrap styling
            )
