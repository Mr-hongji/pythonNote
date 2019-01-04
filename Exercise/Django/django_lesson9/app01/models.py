# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class userInfo(models.Model):
    uname = models.CharField(max_length=100)
    upwd = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=200)