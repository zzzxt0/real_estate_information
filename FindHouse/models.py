from django.db import models

# Create your models here.
# 求租求购信息
class FindHouseInfo(models.Model):
    # 客户名称
    title = models.CharField(max_length=200)

    # 房屋户型
    houseType = models.CharField(max_length=200)

    # 最低价格
    minPrice = models.IntegerField

    # 最高价格
    maxPrice = models.IntegerField

    # 最小房屋大小
    minSize = models.IntegerField

    # 最大房屋大小
    maxSize = models.IntegerField

    # 电梯配置
    Elevator = models.CharField(max_length=10)

    # 装修配置
    renovation = models.CharField(max_length=10)

    #房屋信息类型，求租还是求购
    typeOfMes = models.CharField(max_length=10)

    # 求租/购人真实姓名
    userRealName = models.CharField(max_length=40)

    # 求租/购人联系方式
    userTel = models.CharField(max_length=30)

    # 求租/购人邮箱
    userEmail = models.CharField(max_length=30)

    # 其他房屋要求及描述
    other = models.CharField(max_length=500)

    # 上传信息的用户名——用于外键查找
    userName = models.CharField(max_length=40)
