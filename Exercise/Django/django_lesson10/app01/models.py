# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import Model

class User(Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Hobby(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



'''
ManayToManay 的时候手动生成第三张表

优点：

    使用Django自动生成的第三张表中只有三列：id 和 另外两张表的id,
    使用自己手动生成的第三张表，可以添加其它列

'''

class UserToHobby(Model):
    user = models.ForeignKey(to='User')
    hobby = models.ForeignKey(to='Hobby')
    ctime = models.TimeField()

    '''
    两者联合唯一：
    
    比如：一个人不能有两个相同的爱好
    '''

    class Meta():
        unique_together = [
            ('user', 'hobby'),
        ]
