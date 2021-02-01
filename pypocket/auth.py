import webbrowser
from typing import Union

import requests

from pypocket.pocket_api_endpoints import PocketAPI


class Auth:
    def __init__(self, consumer_key: str):
        self.consumer_key = consumer_key
        self.request_token: Union[str, None] = None
        self.endpoints = PocketAPI

    def get_request_token(self) -> str:
        """Get Request Token from Consumer Key
        Args:

        Returns:
            str: request token
        """
        param = {
            "consumer_key": self.consumer_key,
            "redirect_uri": "http://www.google.com",
        }  # Set POST fields here
        req = requests.get(self.endpoints.oauth_request, param)
        if req.status_code == 200:
            self.request_token = req.content.decode().lstrip("code=")
            return self.request_token

    def authorize_request_token_browser(
        self, request_token: Union[str, None] = None
    ) -> None:
        if request_token is None:
            self.request_token = self.get_request_token()
        else:
            self.request_token = request_token
        auth_url = f"{self.endpoints.auth}?request_token={self.request_token}&redirect_uri=http://www.google.com"
        webbrowser.open(auth_url, new=2)

    def get_access_token(self) -> str:
        """Get Access Token

        Args:

        Returns:
            str: access token
        """
        param = {
            "consumer_key": self.consumer_key,
            "code": self.request_token,
        }  # Set POST fields here

        try:
            resp = requests.get(self.endpoints.oauth_authorize, param)
            resp.raise_for_status()  # Go to Except expression if there is a HTML error

            access_token = resp.content.decode().split("&")[0].lstrip("access_token=")
            return access_token
        except requests.exceptions.HTTPError as err:
            print(err, "\nYou probably have NOT authorized the request token.")
