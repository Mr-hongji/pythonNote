# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    pub_date = models.DateField()
    author = models.CharField(max_length=100)