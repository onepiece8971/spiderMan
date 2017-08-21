from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import multiprocessing


class CrawlerWorker(multiprocessing.Process):
    def __init__(self, spider):
        multiprocessing.Process.__init__(self)
        self.spider = spider
        self.spider.cmd = False
        self.settings = get_project_settings()

    def run(self):
        process = CrawlerProcess(self.settings)
        process.crawl(self.spider)
        process.start()
        process.stop()

    def get_queue(self):
        return self.spider.resultQueue.get()
