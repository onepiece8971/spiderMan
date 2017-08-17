# -*- coding: utf-8 -*-

import scrapy
from scrapy import signals
from multiprocessing.queues import Queue


class BaseSpider(scrapy.Spider):
    items = []
    resultQueue = Queue()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaseSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.resultQueue.put(self.items)

    def _item_append(self, item):
        self.items.append(item)

    def parse(self, response):
        pass
