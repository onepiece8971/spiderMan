# -*- coding: utf-8 -*-

from spiderMan.items import YouDaoItem
from baseSpider import BaseSpider
import scrapy
import json
import re


class YouDaoSpider(BaseSpider):
    name = "youdao"
    allowed_domains = ["dict.youdao.com/"]
    imageUrl = 'https://dict.youdao.com/ugc/wordjson/'
    word = 'apple'
    cmd = True
    # 重试次数
    maxTime = 3

    def __init__(self, *args, **kwargs):
        super(BaseSpider, self).__init__(*args, **kwargs)
        if self.cmd:
            with open('/Users/chenglinz/python/spiderMan/cet4.txt', 'r') as f:
                for line in f:
                    m = re.match(r'^(\w*)/', line)
                    if m:
                        self.start_urls.append("http://dict.youdao.com/w/eng/%s/#keyfrom=dict2.index" % m.group(1))
        else:
            self.start_urls = [
                # 'http://localhost/spiderMan/%s.htm' % self.word,
                "http://dict.youdao.com/w/eng/%s/#keyfrom=dict2.index" % self.word
            ]

    def parse(self, response):
        item = YouDaoItem()
        item['name'] = response.xpath('//*[@id="phrsListTab"]/h2/span/text()').get()
        phsymbol = response.xpath('//*[@id="phrsListTab"]/h2/div/span[2]/span/text()').get()
        item['phsymbol'] = phsymbol if phsymbol else ''
        item['voice'] = 'https://dict.youdao.com/dictvoice?audio=' + item['name'] + '&type=2'
        images = self.http_get(self.imageUrl + item['name'])
        item['images'] = ''
        if len(images) > 0:
            item['images'] = images[0]['Url']
        meaning = response.xpath('//div[@id="phrsListTab"]/div[@class="trans-container"]/ul/li/text()').getall()
        if meaning:
            self.maxTime = 3
            item['meaning'] = json.dumps(meaning)
        elif self.maxTime > 0:
            self.maxTime -= 1
            yield scrapy.Request(response.url, callback=self.parse)
        else:
            item['meaning'] = ''
        sentence = response.xpath('//*[@id="bilingual"]/ul/li/p[descendant-or-self::text()]')
        item['sentence'] = json.dumps(sentence.xpath('normalize-space(string(.))').getall())
        yield item
        self._item_append(item)
