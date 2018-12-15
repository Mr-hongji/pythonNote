# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Classes(models.Model):
    name = models.CharField(max_length=120)
    teacher = models.ManyToManyField('Teachers')


class Students(models.Model):
    name = models.CharField(max_length=120)
    gender = models.BooleanField()
    age = models.IntegerField()
    c = models.ForeignKey(Classes)


class Teachers(models.Model):
    name = models.CharField(max_length=120)
