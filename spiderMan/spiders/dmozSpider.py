# -*- coding: utf-8 -*-

from spiderMan.items import DmozItem
from baseSpider import BaseSpider


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]

    def __init__(self, *args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            # "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
            # "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
            "http://localhost/spiderMan/Books.html",
            "http://localhost/spiderMan/Resources.html",
        ]

    def parse(self, response):
        item = DmozItem()
        item['title'] = response.xpath('//title/text()').get()
        yield item
        self._item_append(item)
