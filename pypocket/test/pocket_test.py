from unittest import TestCase
from unittest.mock import patch

from conftest import sample_list_pocket_items, sample_response
from pypocket.pocket import Pocket


class DerivedPocket(Pocket):
    def __init__(self, customer_key="xyz", access_token="abc"):
        super().__init__(customer_key, access_token)


class MockResponse:
    @staticmethod
    def json():
        return {"list": sample_response()}


class TestPocket(TestCase):
    @patch("pypocket.pocket.requests.get", return_value=MockResponse())
    def test_retrieve(self, mock_get):
        item = DerivedPocket()
        retrieve_results = item.retrieve()

        assert retrieve_results == sample_list_pocket_items()
