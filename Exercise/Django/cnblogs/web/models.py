# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.


'''
null :
    是针对数据库而言，
    如果 null=True, 表示数据库的该字段可以为空，即在Null字段显示为YES。
blank 
    是针对表单的，
    如果 blank=True，表示你的表单填写该字段的时候可以不填，
    但是对数据库来说，没有任何影响
'''


class User(models.Model):
    '''
    用户表
    '''

    uname = models.CharField(verbose_name='用户名', max_length=15)
    pwd = models.CharField(verbose_name='密码', max_length=20)
    img = models.ImageField(verbose_name='用户头像', upload_to='./static/img/userHeadImage')
    uid = models.ManyToManyField('self', verbose_name='用户ID', related_name='Fans', blank=True) # 互粉使用自关联

    # Meta选项 参考： https://www.cnblogs.com/flash55/p/6265405.html
    class Meta:
        db_table = 'User'  # 自定义表名称为User
        verbose_name_plural= '用户' # 指定在admin管理界面中显示的名称

    def __str__(self):
        return self.uname

class Blog(models.Model):
    '''
    博客表
    '''
    title = models.CharField(verbose_name='博客标题', max_length=300)
    summery = models.CharField(verbose_name='博客简介', max_length=300)
    # userid = models.ForeignKey('User', verbose_name='用户ID', unique=True) # 一个人只能开一个博客所以需要唯一
    user = models.OneToOneField('User', verbose_name='用户ID')

    class Meta:
        db_table = 'Blog'  # 自定义表名称为User
        verbose_name_plural= '博客' # 指定在admin管理界面中显示的名称

    def __str__(self):
        return self.title

class Tag(models.Model):
    '''
    博客标签
    '''
    name = models.CharField(verbose_name='标签名', max_length=15)
    blog = models.ForeignKey('Blog', verbose_name='博客ID')

    class Meta:
        db_table = 'Tag'  # 自定义表名称为User
        verbose_name_plural= '标签' # 指定在admin管理界面中显示的名称

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    '''
    博客分类
    '''
    name = models.CharField(verbose_name='分类名', max_length=20)
    blog = models.ForeignKey('Blog', verbose_name='博客ID')

    class Meta:
        db_table = 'BlogCategory'  # 自定义表名称为User
        verbose_name_plural= '博客分类' # 指定在admin管理界面中显示的名称

    def __str__(self):
        return self.name


class WebSitesClassificationLeval(models.Model):
    name = models.CharField(verbose_name='分类名', max_length=32)
    pid = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        db_table = 'WebSitesClassificationLeval'
        verbose_name_plural = '网站分类'

    def __str__(self):
        return self.name




import django.utils.timezone as timezone

class Article(models.Model):
    '''
    文章表
    '''
    title = models.CharField(verbose_name='文章标题', max_length=100)
    summary = models.CharField(verbose_name='文章摘要', max_length=500)
    content = models.CharField(verbose_name='文章内容', max_length=5000)
    createTime = models.DateTimeField(verbose_name='创建时间', null=True, blank=True,
                 auto_now=True)
    blog = models.ForeignKey('Blog', verbose_name='博客ID')
    blogCategory = models.ForeignKey('BlogCategory', verbose_name='博客类别')
    webSiteCategory = models.ForeignKey('WebSitesClassificationLeval', verbose_name='网站类别')
    tag = models.ManyToManyField('Tag', verbose_name='文章标签')

    class Meta:
        db_table = 'Article'  # 自定义表名称为User
        verbose_name_plural= '文章' # 指定在admin管理界面中显示的名称

    def __str__(self):
        return self.title

class UpDown(models.Model):
    '''
    赞或踩
    '''
    upOrDown = models.BooleanField(verbose_name='踩或赞')
    user = models.ForeignKey('User', verbose_name='用户ID')
    article = models.ForeignKey('Article', verbose_name='文章ID')

    class Meta:
        unique_together = [
            ('user', 'article'),
        ]

        db_table = 'UpDown'  # 自定义表名称为User
        verbose_name_plural = '踩赞'  # 指定在admin管理界面中显示的名称

        def __str__(self):
            return self.userId + ',' + self.articleId + ',' + self.upOrDown

class Comment(models.Model):
    '''
    评论
    '''
    user = models.ForeignKey('User', verbose_name='评论者ID', related_name='CommenUid')
    article = models.ForeignKey('Article', verbose_name='文章ID')
    pUser = models.ForeignKey('User', verbose_name='父评论')

    class Meta:
        db_table = 'Comment'  # 自定义表名称为User
        verbose_name_plural = '评论'  # 指定在admin管理界面中显示的名称

    def __str__(self):
        return self.name

class ReportingObstacles(models.Model):
    '''
    报障
    '''
    title = models.CharField(verbose_name='标题', max_length=150)
    content = models.CharField(verbose_name='报障内容', max_length=500)
    commitUser = models.ForeignKey('User', verbose_name='提交者', related_name='commitUserId')
    createTime = models.DateField(verbose_name='创建时间')
    handleUser = models.ForeignKey('User', verbose_name='处理者')
    handleStatus = models.IntegerField(verbose_name='处理状态', default=0)
    handleTime = models.DateField(verbose_name='处理时间')

    class Meta:
        db_table = 'ReportingObstacles'  # 自定义表名称为User
        verbose_name_plural = '报障'  # 指定在admin管理界面中显示的名称

    def __str__(self):
        return self.title


