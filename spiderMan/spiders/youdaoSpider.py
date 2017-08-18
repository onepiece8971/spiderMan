# -*- coding: utf-8 -*-

from spiderMan.items import YouDaoItem
from baseSpider import BaseSpider
import json


class YouDaoSpider(BaseSpider):
    name = "youdao"
    allowed_domains = ["dict.youdao.com/"]
    imageUrl = 'https://dict.youdao.com/ugc/wordjson/'
    word = ''

    def __init__(self, *args, **kwargs):
        super(BaseSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            # 'http://localhost/spiderMan/apple.htm',
            "http://dict.youdao.com/w/eng/" + self.word + "/#keyfrom=dict2.index"
        ]

    def parse(self, response):
        item = YouDaoItem()
        item['name'] = response.xpath('//*[@id="phrsListTab"]/h2/span/text()').get()
        item['phsymbol'] = response.xpath('//*[@id="phrsListTab"]/h2/div/span[2]/span/text()').get()
        item['voice'] = 'https://dict.youdao.com/dictvoice?audio=' + item['name'] + '&type=2'
        images = self.http_get(self.imageUrl + item['name'])
        item['images'] = ''
        if len(images) > 0:
            item['images'] = images[0]['Url']
        item['meaning'] = json.dumps(
            response.xpath('//div[@id="phrsListTab"]/div[@class="trans-container"]/ul/li/text()').getall()
        )
        sentence = response.xpath('//*[@id="bilingual"]/ul/li/p[descendant-or-self::text()]')
        item['sentence'] = json.dumps(sentence.xpath('normalize-space(string(.))').getall())
        yield item
        self._item_append(item)
