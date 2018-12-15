# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 类名代表了数据库表名，且继承了models.Model
class Test(models.Model):

    #  name 代表数据表中的字段 name
    # CharField（相当于varchar）,max_length 参数限定长度
    name = models.CharField(max_length = 20)
