# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_websitesclassificationleval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitesclassificationleval2',
            name='pClassificationId',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='blogId',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='blogCategoryId',
            new_name='blogCategory',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='blogTag',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='userid',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='blogcategory',
            old_name='blogId',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='articleId',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='pUserId',
            new_name='pUser',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='reportingobstacles',
            old_name='commitUserId',
            new_name='commitUser',
        ),
        migrations.RenameField(
            model_name='reportingobstacles',
            old_name='handleUserId',
            new_name='handleUser',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='blogId',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='updown',
            old_name='articleId',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='updown',
            old_name='userId',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='article',
            name='webSiteCategoryId',
        ),
        migrations.AddField(
            model_name='article',
            name='webSiteCategory',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='web.WebSitesClassificationLeval', verbose_name='\u7f51\u7ad9\u7c7b\u522b'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='updown',
            unique_together=set([('user', 'article')]),
        ),
        migrations.DeleteModel(
            name='WebSitesClassificationLeval1',
        ),
        migrations.DeleteModel(
            name='WebSitesClassificationLeval2',
        ),
    ]
