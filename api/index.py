#!/usr/bin/env python

from flask import Flask
from flask_restful import Resource, Api, marshal_with, abort
from spiderMan.crawlerWorker import CrawlerWorker
from spiderMan.spiders import dmozSpider, youdaoSpider
from models.english import English
import re

app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def get(self):
        crawler = CrawlerWorker(dmozSpider.DmozSpider)
        crawler.start()
        items = []
        [items.append(dict(item)) for item in crawler.get_queue()]
        return {'result': 'ok', 'data': items}


class GetEnglish(Resource):
    @marshal_with(English.fields)
    def get(self):
        user = English.query.all()
        return user


class EnglishSpider(Resource):
    def get(self, word):
        m = re.match(r'[a-zA-Z]+', word)
        if not m:
            abort(404, message="word must be alphabet")
        spider = youdaoSpider.YouDaoSpider
        spider.word = word
        crawler = CrawlerWorker(spider)
        crawler.start()
        items = []
        [items.append(dict(item)) for item in crawler.get_queue()]
        return {'result': 'ok', 'data': items}


api.add_resource(Test, '/test')
api.add_resource(GetEnglish, '/')
api.add_resource(EnglishSpider, '/scra/<string:word>')

if __name__ == '__main__':
    app.run(debug=True)
