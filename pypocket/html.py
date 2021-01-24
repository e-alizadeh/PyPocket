from typing import List

import dominate
from dominate import tags

from pypocket.pocket import PocketItem


class HTML:
    def __init__(self):
        self.doc = dominate.document(title="Pocket Items")

    def _add_item(self, pocket_item: PocketItem):
        self.doc.add(tags.h3(pocket_item.title, cls="defaultfontfamily"))

        # Add bullets
        pocket_item_description = tags.ul()

        pocket_item_description += tags.li(
            "Link: ",
            tags.a(pocket_item.url, href=pocket_item.url),
            cls="defaultfontfamily",
        )
        pocket_item_description += tags.li(
            "Tags: ",
            ", ".join([elem for elem in pocket_item.tags]),
            cls="defaultfontfamily",
        )
        pocket_item_description += tags.li(
            "Time added: ",
            pocket_item.convert_datetime_to_string(pocket_item.time_added),
            cls="defaultfontfamily",
        )

        self.doc.add(pocket_item_description)

    def get_html_str(self, list_pocket_items: List[PocketItem]) -> str:
        with self.doc.head:
            tags.style(
                ".defaultfontfamily {font-family: Lucida Sans Unicode,Lucida Grande,sans-serif;}",
                type="text/css",
            )

        for item in list_pocket_items:
            self._add_item(item)

        return self.doc.render()
