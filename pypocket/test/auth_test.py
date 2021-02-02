from unittest import TestCase
from unittest.mock import patch

from pypocket.auth import Auth


class FakeResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.content = self.json_data["content"]

    def raise_for_status(self):
        if self.status_code == 200:
            return None
        else:
            return self.json_data["error"]


class TestAuth(TestCase):
    @patch("pypocket.auth.requests.get")
    def test_get_request_token(self, mock_request):
        mock_request.return_value = FakeResponse(
            {"content": b"code=random_request_token"}, 200
        )

        class DerivedAuth(Auth):
            def __init__(self, customer_key="abc"):
                super().__init__(customer_key)

        request_token = DerivedAuth().get_request_token()
        assert request_token == "random_request_token"

    @patch("pypocket.auth.requests.get")
    def test_get_access_token(self, mock_request):
        mock_request.return_value = FakeResponse(
            {"content": b"access_token=random_access_token&username=abc"}, 200
        )

        class DerivedAuth(Auth):
            def __init__(self, customer_key="abc"):
                super().__init__(customer_key)
                self.request_token = "xyz"

        access_token = DerivedAuth().get_access_token()
        assert access_token == "random_access_token"
