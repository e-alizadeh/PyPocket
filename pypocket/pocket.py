from typing import Dict, List

import requests

from pypocket.html import HTML
from pypocket.pocket_api_endpoints import PocketAPI
from pypocket.pocket_dataclass import PocketItem
from pypocket.utils import convert_epoch_to_utc_datetime


class Pocket(object):
    def __init__(
        self, consumer_key: str, access_token: str, html_filename: str = "report"
    ):
        self._consumer_key = consumer_key
        self._access_token = access_token
        self.pocket_endpoints = PocketAPI

        self.html_document = HTML()

        # Handle both scenarios where the html_filename has either .html extension or not.
        self.html_output_filename = (
            html_filename
            if html_filename.endswith(".html")
            else f"{html_filename}.html"
        )

    @staticmethod
    def _reformat_items(item: Dict[str, str]) -> PocketItem:
        """Convert a Pocket item data structure from dictionary to custom data structure PocketItem

        Args:
            item (Dict[str, str]): The content of a pocket item

        Returns:
            PocketItem
        """
        return PocketItem(
            item_id=int(item["item_id"]),
            title=item["resolved_title"],
            url=item["resolved_url"],
            tags=list(item["tags"]) if "tags" in item.keys() else [],
            time_added=convert_epoch_to_utc_datetime(int(item["time_added"])),
            time_updated=convert_epoch_to_utc_datetime(int(item["time_updated"])),
        )

    def retrieve(self, num_post: int = 5) -> List[PocketItem]:
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

    def to_html(self, num_post: int = 5) -> None:
        with open(f"./{self.html_output_filename}", "w", encoding="utf-8") as f:
            f.write(
                self.html_document.get_html_str(
                    list_pocket_items=self.retrieve(num_post)
                )
            )
