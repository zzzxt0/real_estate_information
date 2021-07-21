import scrapy
from beike.items import BeikeItem

# 二手房
class BeikespiderSpider(scrapy.Spider):

    name = 'beikespider'
    start_urls = []
    for i in range(101):
        start_urls.append('https://nb.lianjia.com/ershoufang/pg'+str(i)+'/')

    def start_requests(self):
        for d in self.start_urls:
            yield scrapy.Request(d, callback=self.parse)

    def parse(self, response):
        data_list = response.xpath('//div/ul[@class="sellListContent"]/li')
        for data in data_list:
            item = BeikeItem()
            item['title'] = data.xpath('.//div[@class="title"]/a/text()').extract_first()
            item['houseurl'] = data.xpath('.//div[@class="title"]/a/@href').extract_first()
            item['photo'] = data.xpath('.//img[2]/@src').extract_first()

            item['location'] = data.xpath('.//div[@class="positionInfo"]/a/text()').extract_first()
            item['totalprice'] = str(data.xpath('.//div[@class="totalPrice"]//text()').extract_first())
            # print(item)
            # yield(item)
            yield scrapy.Request(url=item['houseurl'], callback=self.parse_detail, meta={"item": item})

    # 解析二级页面
    def parse_detail(self, response):
        item = response.meta["item"]
        datalist = response.xpath('//body')
        for data in datalist:
            item['huxing'] = data.xpath('.//div[@class="base"]//div[@class="content"]/ul/li[1]/text()').extract_first()
            item['floor'] = data.xpath('.//div[@class="base"]//div[@class="content"]/ul/li[2]/text()').extract_first()
            item['area'] = data.xpath('.//div[@class="base"]//div[@class="content"]/ul/li[3]/text()').extract_first()
            item['chaoxiang'] = data.xpath('.//div[@class="base"]//div[@class="content"]/ul/li[7]/text()').extract_first()
            item['zhuangxiu'] = data.xpath('.//div[@class="base"]//div[@class="content"]/ul/li[9]/text()').extract_first()
            item['elevator'] = data.xpath('.//div[@class="base"]//div[@class="content"]/ul/li[11]/text()').extract_first()
            item['unitPrice'] = data.xpath('.//span[@class="unitPriceValue"]//text()').extract_first()
            print(item)
        return item