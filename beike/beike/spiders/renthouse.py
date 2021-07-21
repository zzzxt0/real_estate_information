import scrapy
from beike.items import RenthouseItem

# 租房
class RenthouseSpider(scrapy.Spider):
    name = 'renthouse'
    start_urls = []
    for i in range(101):
        start_urls.append('https://nb.lianjia.com/zufang/pg' + str(i) + '/')

    def start_requests(self):
        for d in self.start_urls:
            yield scrapy.Request(d, callback=self.parse)

    def parse(self, response):
        data_list = response.xpath('//div[@class="content__list"]//div[@class="content__list--item"]')

        for data in data_list:
            item = RenthouseItem()
            item['title'] = data.xpath('normalize-space(.//p[@class="content__list--item--title"]/a/text())').extract_first()
            item['houseurl'] = 'https://nb.lianjia.com/' + data.xpath(
                './/p[@class="content__list--item--title"]/a/@href').extract_first()
            item['photo'] = data.xpath('.//a[@class="content__list--item--aside"]/img/@data-src').extract_first()
            item['location'] = data.xpath(
                './/p[@class="content__list--item--des"]/a[1]/text()').extract_first() + data.xpath(
                './/p[@class="content__list--item--des"]/a[2]/text()').extract_first() + data.xpath(
                './/p[@class="content__list--item--des"]/a[3]/text()').extract_first()

            item['price'] = data.xpath('.//span[@class="content__list--item-price"]/em/text()').extract_first()

            item['floor'] = data.xpath('.//span[@class="hide"]//text()').extract()[2].replace(' ', '').replace('\n', '')
            item['area'] = data.xpath('.//p[@class="content__list--item--des"]//text()').extract()[8].replace(' ', '').replace('\n', '')

            item['huxing'] = data.xpath('.//p[@class="content__list--item--des"]//text()').extract()[12].replace(' ', '').replace('\n', '')
            item['chaoxiang'] = data.xpath('.//p[@class="content__list--item--des"]//text()').extract()[10].replace(' ', '')
            yield (item)
