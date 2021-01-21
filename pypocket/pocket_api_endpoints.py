from dataclasses import dataclass


@dataclass
class PocketAPI:
    """Class for official GetPocket API endpoints"""

    api: str = "https://getpocket.com"
    get: str = api + "/v3/get"
