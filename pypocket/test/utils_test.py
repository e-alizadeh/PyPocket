from datetime import datetime

from ..utils import convert_epoch_to_human_readable_date, convert_epoch_to_utc_datetime


def test_convert_epoch_to_utc_datetime():
    epoch = 1610904106
    computed_output = convert_epoch_to_utc_datetime(epoch)
    expected_output = datetime(2021, 1, 17, 17, 21, 46)
    assert computed_output == expected_output


def test_convert_epoch_to_human_readable_date():
    epoch = 1610904106
    computed_output = convert_epoch_to_human_readable_date(epoch)
    expected_output = "Sun, 17 Jan 2021"
    assert computed_output == expected_output
