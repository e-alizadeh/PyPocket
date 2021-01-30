from typing import Any, Dict, List

from pypocket.pocket_dataclass import PocketItem
from pypocket.utils import convert_epoch_to_utc_datetime


# @pytest.fixture()
def sample_response() -> Dict[str, Any]:
    fake_response_get = {
        "123": {
            "item_id": "123",
            "resolved_id": "123",
            "given_url": "https://google.com",
            "given_title": "",
            "favorite": "0",
            "status": "0",
            "time_added": "1611279297",
            "time_updated": "1611279297",
            "time_read": "0",
            "time_favorited": "0",
            "sort_id": 0,
            "resolved_title": "This is the title of post 1",
            "resolved_url": "https://google.com",
            "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "is_article": "1",
            "is_index": "0",
            "has_video": "0",
            "has_image": "1",
            "word_count": "100",
            "lang": "en",
            "time_to_read": 3,
        },
        "456": {
            "item_id": "456",
            "resolved_id": "456",
            "given_url": "https://abc.xyz",
            "given_title": "",
            "favorite": "0",
            "status": "0",
            "time_added": "1611120874",
            "time_updated": "1611205801",
            "time_read": "0",
            "time_favorited": "0",
            "sort_id": 0,
            "resolved_title": "This is the title of post 2",
            "resolved_url": "https://abc.xyz",
            "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "is_article": "1",
            "is_index": "0",
            "has_video": "0",
            "has_image": "1",
            "word_count": "200",
            "lang": "en",
            "time_to_read": 5,
            "tags": {
                "python": {"item_id": "456", "tag": "python"},
                "modeling": {"item_id": "456", "tag": "modeling"},
            },
        },
    }

    return fake_response_get


# @pytest.fixture()
def expected_list_pocket_items() -> List[PocketItem]:
    return [
        PocketItem(
            item_id=123,
            title="This is the title of post 1",
            url="https://google.com",
            tags=[],
            time_added=convert_epoch_to_utc_datetime(1611279297),
            time_updated=convert_epoch_to_utc_datetime(1611279297),
        ),
        PocketItem(
            item_id=456,
            title="This is the title of post 2",
            url="https://abc.xyz",
            tags=["python", "modeling"],
            time_added=convert_epoch_to_utc_datetime(1611120874),
            time_updated=convert_epoch_to_utc_datetime(1611205801),
        ),
    ]
