from django.db import models


# Create your models here.
class HouseInfo(models.Model):
    location = models.CharField(max_length=100)

# 用户信息
class User(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phoneNumber = models.CharField(max_length=200)

    # 密码
    passWord = models.CharField(max_length=200)

