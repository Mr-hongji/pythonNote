# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20190312_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='createTime',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
