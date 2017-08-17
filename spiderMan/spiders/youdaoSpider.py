# -*- coding: utf-8 -*-

from spiderMan.items import YouDaoItem
from baseSpider import BaseSpider


class YouDaoSpider(BaseSpider):
    name = "youdao"
    allowed_domains = ["dict.youdao.com/"]

    def __init__(self, *args, **kwargs):
        super(YouDaoSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            "http://dict.youdao.com/w/apple/#keyfrom=dict2.top",
        ]

    def parse(self, response):
        item = YouDaoItem()
        item['name'] = response.xpath('//*[@id="phrsListTab"]/h2/span/text()').get()
        yield item
        self._item_append(item)
