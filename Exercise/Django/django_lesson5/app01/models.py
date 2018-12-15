# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    publishdata = models.DateField()
    publiser = models.ForeignKey('Publish')

    # 使用 ManyToManyField 创建多对多关系， 会自动生成第三张表
    author = models.ManyToManyField('Author')

    # 手动创建第三张表，其实就是创建外键方式
    # publiser = models.ForeignKey('Author')

class Publish(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)


class Author(models.Model):
    name = models.CharField(max_length=120)

