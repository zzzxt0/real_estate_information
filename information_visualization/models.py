from django.db import models


# Create your models here.
class HouseInfo(models.Model):
    location = models.CharField(max_length=100)
