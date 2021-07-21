# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 二手房
# class BeikeItem(scrapy.Item):
#     title = scrapy.Field()  # 房产标题
#     location = scrapy.Field()  # 位置
#     totalprice = scrapy.Field()  # 售价
#     houseurl = scrapy.Field()  # 二级页面链接
#     photo = scrapy.Field()  # 图片路径
#     huxing = scrapy.Field()  # 户型
#     floor = scrapy.Field()  # 楼层
#     area = scrapy.Field()  # 面积
#     chaoxiang = scrapy.Field()  # 朝向
#     zhuangxiu = scrapy.Field()  # 装修
#     elevator = scrapy.Field()  # 有无电梯
#     unitPrice = scrapy.Field()  # 单价
#     pass
from scrapy_djangoitem import DjangoItem
from information_visualization.models import HouseInfo, NewhouseItem, RenthouseItem


# 二手房
class BeikeItem(DjangoItem):
    django_model = HouseInfo
    pass

# 新房
# class NewhouseItem(scrapy.Item):
#     title = scrapy.Field()  # 房产标题
#     location = scrapy.Field()  # 位置
#     totalprice = scrapy.Field()  # 售价
#     area = scrapy.Field()  # 面积
#     houseurl = scrapy.Field()  # 二级页面链接
#     photo = scrapy.Field()  # 图片路径
#     huxing = scrapy.Field()  # 户型
#     unitPrice = scrapy.Field()  # 单价
#     pass

# 新房
class NewhouseItem(DjangoItem):
    django_model = NewhouseItem
    pass


# 租房
# class RenthouseItem(scrapy.Item):
#     title = scrapy.Field()  # 房产标题
#     location = scrapy.Field()  # 位置
#     huxing = scrapy.Field()  # 户型
#     area = scrapy.Field()  # 面积
#     chaoxiang = scrapy.Field()  # 朝向
#     price = scrapy.Field()  # 价格
#     houseurl = scrapy.Field()  # 二级页面链接
#     photo = scrapy.Field()  # 图片路径
#     floor = scrapy.Field()  # 楼层
#     pass

# 租房
class RenthouseItem(DjangoItem):
    django_model = RenthouseItem
    pass