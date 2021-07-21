from django.db import models


# Create your models here.
# 二手房
class HouseInfo(models.Model):
    title = models.CharField(max_length=100)  # 房产标题
    location = models.CharField(max_length=100)  # 位置
    totalprice = models.CharField(max_length=20)  # 售价
    houseurl = models.CharField(max_length=255)  # 二级页面链接
    photo = models.CharField(max_length=255)  # 图片路径
    huxing = models.CharField(max_length=30)  # 户型
    floor = models.CharField(max_length=10)  # 楼层
    area = models.CharField(max_length=10)  # 面积
    chaoxiang = models.CharField(max_length=10)  # 朝向
    zhuangxiu = models.CharField(max_length=10)  # 装修
    elevator = models.CharField(max_length=5)  # 有无电梯
    unitPrice = models.CharField(max_length=100)  # 单价

# 新房
class NewhouseItem(models.Model):
    title = models.CharField(max_length=100)  # 房产标题
    location = models.CharField(max_length=100)  # 位置
    totalprice = models.CharField(max_length=20)  # 售价
    houseurl = models.CharField(max_length=255)  # 二级页面链接
    photo = models.CharField(max_length=255)  # 图片路径
    huxing = models.CharField(max_length=30)  # 户型
    area = models.CharField(max_length=10)  # 面积
    unitPrice = models.CharField(max_length=100)  # 单价

# 租房
class RenthouseItem(models.Model):
    title = models.CharField(max_length=100)  # 房产标题
    location = models.CharField(max_length=100)  # 位置
    houseurl = models.CharField(max_length=255)  # 二级页面链接
    photo = models.CharField(max_length=255)  # 图片路径
    huxing = models.CharField(max_length=30)  # 户型
    area = models.CharField(max_length=10)  # 面积
    price = models.CharField(max_length=100)  # 价格
    floor = models.CharField(max_length=10)  # 楼层
    chaoxiang = models.CharField(max_length=10)  # 朝向

# 用户信息
class User(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phoneNumber = models.CharField(max_length=200)

    # 密码
    passWord = models.CharField(max_length=200)

