# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.db.models import Count, Min, Sum, Avg
from django.db.models import Q,F
from util import multilevelCategoryMenu, util, pagination
from django.utils.safestring import mark_safe

import json
import datetime
import models

def index(request):
    '''
    返回首页
    :param request:
    :return:
    '''

    s = 'ASDF'
    print(list(s))
    pager = getPagination(0)
    paginatorResult = mark_safe(pager.paginatorResult)

    articles = queryAllArticle((pager.currentPage - 1) * pager.pageSize, pager.currentPage * pager.pageSize)

    return render(request, 'index.html', locals())

def getClassficationData(request):
    '''
    获取网站左侧的分类菜单数据
    :param request:
    :return:
    '''
    ret = multilevelCategoryMenu.queryMultilevelCategoryMenu()
    return HttpResponse(ret)

class article(object):
    def __init__(self, id, title, summary, content, ctime, uname):
        self.id = id
        self.uname = uname
        self.title = title
        self.summary = summary
        self.content = content
        self.ctime = ctime

def queryAllArticle(start, end):

    allArticle = models.Article.objects.all()[start:end]

    ret = []
    for article in allArticle:

        # 格式化日期时间
        ctime = util.formatDataTime( article.createTime)

        ret.append({'id':article.id, 'title': article.title,
                     'summery': article.summary, 'content': article.content,
                     'createTime':ctime , 'uname':article.blog.user.uname})

    return ret


def getPagination(currentPage):
    '''
        :param currentPage: 当前页数
        :param pageSize: 每页显示条数
   '''

    paginationRet = pagination.page(models.Article.objects.count(), currentPage)

    return paginationRet