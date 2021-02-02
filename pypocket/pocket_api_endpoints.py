from dataclasses import dataclass


@dataclass
class PocketAPI:
    """Class for official GetPocket API endpoints"""

    base_url: str = "https://getpocket.com"
    get: str = base_url + "/v3/get"
    auth: str = base_url + "/auth/authorize"
    oauth_request: str = base_url + "/v3/oauth/request"
    oauth_authorize: str = base_url + "/v3/oauth/authorize"
