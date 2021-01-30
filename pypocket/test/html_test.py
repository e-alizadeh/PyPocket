from unittest import TestCase

from conftest import sample_list_pocket_items
from pypocket.html import HTML


class TestHTML(TestCase):
    def test_html(self):
        html = HTML()
        computed_output = html.get_html_str(sample_list_pocket_items())
        expected_output = (
            "<!DOCTYPE html>\n<html>\n  "
            "<head>\n    "
            "<title>Pocket Items</title>\n    "
            '<style type="text/css">.defaultfontfamily '
            "{font-family: Lucida Sans Unicode,Lucida Grande,sans-serif;}"
            "</style>\n  "
            "</head>\n  "
            "<body>\n    "
            '<h3 class="defaultfontfamily">This is the title of post 1</h3>\n    '
            "<ul>\n      "
            '<li class="defaultfontfamily">Link: \n        '
            '<a href="https://google.com">https://google.com</a>\n      </li>\n      '
            '<li class="defaultfontfamily">Tags: </li>\n      '
            '<li class="defaultfontfamily">Time added: Fri, 22 Jan 2021</li>\n    '
            "</ul>\n    "
            '<h3 class="defaultfontfamily">This is the title of post 2</h3>\n    '
            "<ul>\n      "
            '<li class="defaultfontfamily">Link: \n        '
            '<a href="https://abc.xyz">https://abc.xyz</a>\n      </li>\n      '
            '<li class="defaultfontfamily">Tags: python, modeling</li>\n      '
            '<li class="defaultfontfamily">Time added: Wed, 20 Jan 2021</li>\n    '
            "</ul>\n  "
            "</body>\n"
            "</html>"
        )

        assert computed_output == expected_output
