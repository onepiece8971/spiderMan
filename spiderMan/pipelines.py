# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs


class DmozPipeline(object):
    def __init__(self):
        self.file = codecs.open('dmoz.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        # print line
        self.file.write(line.decode("unicode_escape"))
        return item


class YouDaoPipeline(object):
    def __init__(self):
        from api.models.english import English
        self.englishModel = English

    def process_item(self, item, spider):
        re_id = self.englishModel.insert_english(item)
        if re_id:
            print '\033[1;32mSuccess:\033[0m %s' % item['name']
        else:
            print '\033[1;31mError:\033[0m %s' % item['name']

        return item
