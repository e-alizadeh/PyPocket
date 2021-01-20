from ..utils import convert_epoch_to_human_readable_datetime


def test_convert_epoch_to_human_readable_datetime():
    epoch = 1610904106
    computed_output = convert_epoch_to_human_readable_datetime(epoch)
    expected_output = "Sun, 17 Jan 2021 12:21:46 EST"
    assert computed_output == expected_output
