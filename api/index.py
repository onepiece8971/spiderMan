#!/usr/bin/env python

from flask import Flask
from flask_restful import Resource, Api, marshal_with
from spiderMan.crawlerWorker import CrawlerWorker
from spiderMan.spiders import dmozSpider, youdaoSpider
from models.english import English

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
    def get(self):
        crawler = CrawlerWorker(youdaoSpider.YouDaoSpider)
        crawler.start()
        items = []
        [items.append(dict(item)) for item in crawler.get_queue()]
        return {'result': 'ok', 'data': items}


api.add_resource(Test, '/test')
api.add_resource(GetEnglish, '/')
api.add_resource(EnglishSpider, '/scra')

if __name__ == '__main__':
    app.run(debug=True)
