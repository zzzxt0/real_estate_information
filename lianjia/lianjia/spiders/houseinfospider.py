import scrapy
from lianjia.lianjia.items import LianjiaItem


class HouseinfospiderSpider(scrapy.Spider):
    name = 'houseinfospider'
    allowed_domains = ['m.lianjia.com']
    start_urls = ['http://m.lianjia.com/']

    def parse(self, response):
        house = LianjiaItem()
        pass
