# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-20 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassToTeaher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='classtoteaher',
            name='hobby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Hobby'),
        ),
        migrations.AddField(
            model_name='classtoteaher',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User'),
        ),
        migrations.AlterUniqueTogether(
            name='classtoteaher',
            unique_together=set([('user', 'hobby')]),
        ),
    ]
