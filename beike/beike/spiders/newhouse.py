import scrapy
from beike.items import NewhouseItem

# 新房
class NewhouseSpider(scrapy.Spider):
    name = 'newhouse'
    start_urls = []
    for i in range(24):
        start_urls.append('https://nb.fang.lianjia.com/loupan/nhs1pg'+str(i)+'/')

    def start_requests(self):
        for d in self.start_urls:
            yield scrapy.Request(d, callback=self.parse)

    def parse(self, response):
        data_list = response.xpath('//div/ul[@class="resblock-list-wrapper"]/li')

        for data in data_list:
            item = NewhouseItem()
            item['title'] = data.xpath('.//div[@class="resblock-name"]/a/text()').extract_first()
            item['houseurl'] = 'https://nb.fang.lianjia.com'+data.xpath('.//div[@class="resblock-name"]/a/@href').extract_first()
            item['photo'] = data.xpath('.//a[@class="resblock-img-wrapper "]/img/@data-original').extract_first()
            item['area'] = ''
            if data.xpath('.//div[@class="resblock-area"]/span/text()').extract_first()[3:]:
                item['area'] = item['area']+data.xpath('.//div[@class="resblock-area"]/span/text()').extract_first()[3:]
            item['location'] = data.xpath('.//div[@class="resblock-location"]//text()').extract()[-2]
            huxingstr = ''
            for i in range(1, len(data.xpath('.//a[@class="resblock-room"]//text()').extract()), 2):
                huxingstr = huxingstr + data.xpath('.//a[@class="resblock-room"]//text()').extract()[i]
            item['huxing'] = huxingstr
            # item['huxing'] = data.xpath('.//a[@class="resblock-room"]//text()').extract()
            item['totalprice'] = data.xpath('.//div[@class="resblock-price"]//div[@class="second"]/text()').extract_first()[2:]
            item['unitPrice'] = data.xpath('.//div[@class="resblock-price"]//div[@class="main-price"]//span/text()').extract_first()
            yield(item)
