# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-28 04:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('summary', models.CharField(max_length=500, verbose_name='\u6587\u7ae0\u6458\u8981')),
                ('content', models.CharField(max_length=5000, verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('createTime', models.DateField(blank=True, default=b'2019-02-28 12:37:52', null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'Article',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='\u535a\u5ba2\u6807\u9898')),
                ('summery', models.CharField(max_length=300, verbose_name='\u535a\u5ba2\u7b80\u4ecb')),
            ],
            options={
                'db_table': 'Blog',
                'verbose_name_plural': '\u535a\u5ba2',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5206\u7c7b\u540d')),
                ('blogId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Blog', verbose_name='\u535a\u5ba2ID')),
            ],
            options={
                'db_table': 'BlogCategory',
                'verbose_name_plural': '\u535a\u5ba2\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Article', verbose_name='\u6587\u7ae0ID')),
            ],
            options={
                'db_table': 'Comment',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='ReportingObstacles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='\u6807\u9898')),
                ('content', models.CharField(max_length=500, verbose_name='\u62a5\u969c\u5185\u5bb9')),
                ('createTime', models.DateField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('handleStatus', models.IntegerField(default=0, verbose_name='\u5904\u7406\u72b6\u6001')),
                ('handleTime', models.DateField(verbose_name='\u5904\u7406\u65f6\u95f4')),
            ],
            options={
                'db_table': 'ReportingObstacles',
                'verbose_name_plural': '\u62a5\u969c',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='\u6807\u7b7e\u540d')),
                ('blogId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Blog', verbose_name='\u535a\u5ba2ID')),
            ],
            options={
                'db_table': 'Tag',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='UpDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upOrDown', models.BooleanField(verbose_name='\u8e29\u6216\u8d5e')),
                ('articleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Article', verbose_name='\u6587\u7ae0ID')),
            ],
            options={
                'db_table': 'UpDown',
                'verbose_name_plural': '\u8e29\u8d5e',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=15, verbose_name='\u7528\u6237\u540d')),
                ('pwd', models.CharField(max_length=20, verbose_name='\u5bc6\u7801')),
                ('img', models.ImageField(upload_to='./static/img/userHeadImage', verbose_name='\u7528\u6237\u5934\u50cf')),
                ('uid', models.ManyToManyField(blank=True, related_name='_user_uid_+', to='web.User', verbose_name='\u7528\u6237ID')),
            ],
            options={
                'db_table': 'User',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='WebSitesClassificationLeval1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5206\u7c7b\u540d')),
            ],
            options={
                'db_table': 'WebSitesClassificationLeval1',
                'verbose_name_plural': '\u7f51\u7ad9\u4e00\u7ea7\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='WebSitesClassificationLeval2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5206\u7c7b\u540d')),
                ('pClassificationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.WebSitesClassificationLeval1', verbose_name='\u7236\u7ea7\u5206\u7c7b')),
            ],
            options={
                'db_table': 'WebSitesClassificationLeval2',
                'verbose_name_plural': '\u7f51\u7ad9\u4e8c\u7ea7\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='updown',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User', verbose_name='\u7528\u6237ID'),
        ),
        migrations.AddField(
            model_name='reportingobstacles',
            name='commitUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commitUserId', to='web.User', verbose_name='\u63d0\u4ea4\u8005'),
        ),
        migrations.AddField(
            model_name='reportingobstacles',
            name='handleUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User', verbose_name='\u5904\u7406\u8005'),
        ),
        migrations.AddField(
            model_name='comment',
            name='pUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User', verbose_name='\u7236\u8bc4\u8bba'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommenUid', to='web.User', verbose_name='\u8bc4\u8bba\u8005ID'),
        ),
        migrations.AddField(
            model_name='blog',
            name='userid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.User', verbose_name='\u7528\u6237ID'),
        ),
        migrations.AddField(
            model_name='article',
            name='blogCategoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.BlogCategory', verbose_name='\u535a\u5ba2\u7c7b\u522b'),
        ),
        migrations.AddField(
            model_name='article',
            name='blogId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Blog', verbose_name='\u535a\u5ba2ID'),
        ),
        migrations.AddField(
            model_name='article',
            name='blogTag',
            field=models.ManyToManyField(to='web.Tag', verbose_name='\u6587\u7ae0\u6807\u7b7e'),
        ),
        migrations.AddField(
            model_name='article',
            name='webSiteCategoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.WebSitesClassificationLeval2', verbose_name='\u7f51\u7ad9\u7c7b\u522b'),
        ),
        migrations.AlterUniqueTogether(
            name='updown',
            unique_together=set([('userId', 'articleId')]),
        ),
    ]