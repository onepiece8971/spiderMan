# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidermanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class YouDaoItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    phsymbol = scrapy.Field()
    voice = scrapy.Field()
    images = scrapy.Field()
    meaning = scrapy.Field()
    sentence = scrapy.Field()
