# -*- coding:utf-8 -*-

'''
查询多级分类数据工具类
'''


import json
from web import models
from django.db.models import Q,F
from django.db.models import Count, Min, Sum, Avg


class classificationObj(object):
    '''
    网站左侧的分类菜单类
    '''
    child =None
    def __init__(self, id, name):
        self.id = id
        self.name = name

def classification2Dic(item):
    '''
    classificationObj对象序列化
    :param item:
    :return:
    '''
    return {
        'id':item.id,
        'name':item.name,
        'child':item.child
    }

def queryMultilevelCategoryMenu():
    '''
    获取网站左侧的分类菜单数据
    :param request:
    :return:
    '''

    classifications = models.WebSitesClassificationLeval.objects.values().order_by('-id').filter(pid=F('id'))
    print (classifications)

    classficationItems = []

    for item in classifications:
        classification = classificationObj(item['id'], item['name'])

        childItems = models.WebSitesClassificationLeval.objects.values().order_by('-id').filter(Q(pid=classification.id) & ~Q(id=classification.id))

        classification.child = list(childItems)

        classficationItems.append(classification)

    print (classficationItems)
    ret = json.dumps(classficationItems, encoding='utf-8', ensure_ascii=False, default=classification2Dic)
    return ret


