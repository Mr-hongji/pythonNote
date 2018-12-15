# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from app01.models import Book, Publish, Author

from django.db.models import Q, F

# Create your views here.

import json

def one_to_maney(request):

    '''
    一对多
    :param request:
    :return:
    '''

    # 插入数据
    # 方式一：
    # p = Publish.objects.filter(name='海南出版社')[0]
    # Book.objects.create(name='倾城之恋', price=62, publishdata='1943-01-25', publiser=p, author='张爱玲')
    # # 方式二
    # p = Publish.objects.filter(name='河北人民出版社')[0]
    # Book.objects.create(name = '雷雨', price=25, publishdata='1934-07-01', publiser_id=p.id, author='曹禺')

    # 删除全部
    # Book.objects.all().delete()

    # 查询北京大学出版社出版的书
    # 方式一 正向查询
    p = Publish.objects.filter(name='北京大学出版社')[0]
    ret = Book.objects.filter(publiser = p).values('name')

    # 方式二 反向查询
    p = Publish.objects.filter(name='北京大学出版社')[0]
    print(p.book_set.all().values('name', 'price'))

#------------------------------------------- 万能双下划綫 -------------------------------------------
    # 方式三
    ret = Book.objects.filter(publiser__name='北京大学出版社').values('price', 'name')

    # 查询 java 这本书出版社的名字
    # 方式一
    ret = Book.objects.filter(name='java').values('publiser__name')
    # 方式二 反向查询
    ret = Publish.objects.filter(book__name='java').values('name')

    # 查询 1990 - 1991 年出版的书的出版社名字
    ret = Book.objects.filter(publishdata__gte ='1990-01-01', publishdata__lte='1991-12-31').values('publiser__name')


    printRes(ret)

    return HttpResponse('Success!')



def many_to_many(request):
    '''
    多对多
    :param request:
    :return:
    '''

    # 给骆驼祥子这本书添加作者老舍
    author_obj = Author.objects.get(name='老舍')
    book_obj = Book.objects.get(name='骆驼祥子')
    book_obj.author.add(author_obj)

    # 给骆驼祥子这本书添加 id=1 的作者
    book_obj.author.add(1)
    #添加 id 等于 2 和 3 的作者
    book_obj.author.add([2,3])

    # 给骆驼祥子这本书重新设置 id 等于 2、3、4 的作者
    # 执行完成后第三张表中原本已存在的作者 id 等于 2、3 的数据不变，同时会新增一条 作者id  等于 4 的记录
    book_obj.author.set([2,3,4])

    # 移除 id 等于 1 的作者
    book_obj.author.remove(1)
    # 移除 id 等于 2 和 3 的作者
    book_obj.author.remove([2,3])

    # 清除这本书的所有作者， 清除后第三张表中不存在 骆驼祥子这本书的对应关系记录了
    book_obj.author.clear()

    # 给 id = 17 的这本书添加所有作者 （*author_objs）
    author_objs = Author.objects.all()
    book_obj = Book.objects.get(id=17)
    book_obj.author.add(*author_objs)

    # 删除 id = 17 这本书中 id = 1 的作者
    book_obj.author.remove(1)

    # 删除 id = 17 的这本书的所有作者 （*author_objs）
    book_obj.author.remove(*author_objs)


    # 反向添加
    # 给老舍添加骆驼祥子这本书
    author_obj = Author.objects.filter(name="老舍")
    book_obj = Book.objects.filter(name="骆驼祥子")
    author_obj.book_set.add(book_obj)
    # 给 id=1 的作者添加 id=2 的这本书
    author_obj = Author.objects.filter(id='1')
    author_obj.book_set.add(2)

    # 查询 id = 17 这本书的所有作者
    # 正向查询
    book_obj = Book.objects.get(id=17)
    author_objs = book_obj.author.all()
    print(author_objs)

    # 反向查询
    # 查询 id = 1 这个作者出过的所有书
    author_obj = Author.objects.get(id=1)
    books = author_obj.book_set.all()
    print(books)

    for item in books:
        print(item.name)

    # 反向跨表查询
    # 查询所有作者的书籍
    author_objs = Author.objects.values("id", "name", "book_set__name")




    # 查询 老舍 出的书的名称和价格
    books = Book.objects.filter(author__name='老舍').values('name', 'price')
    printRes(books)

    return HttpResponse('Success!')



def q_f(request):

    '''
    使用  Q 和 F 查询需要导入：from django.db.models import Q, F

    Q查询：
        可以使用  |（or）  、  & （and） 连接成一个新的Q对象，还支持用  ~   符号取反

    F查询：
        1、进行加、减、乘、除、取模、幂计算等操作
        2、支持双下划线进行连表查询

    :param request:
    :return:
    '''
    # 这种方式只能是并且关系查询（查询书名是 PHP 并且 出版社id = 1 的书）
    books = Book.objects.filter(name='PHP', publiser_id=1)
    # 等同于
    Book.objects.filter(Q(name='PHP') | Q(publiser_id=1))


    # 使用 Q 进行逻辑查询
    # 查询书名是 PHP 或 出版社id = 1 的书
    books = Book.objects.filter(Q(name='PHP') | Q(publiser_id=1))

    # 查询书名是 PHP 出版社 id 是 1 或者 价格大于 25 的书
    books = Book.objects.filter((Q(name='PHP') & Q(publiser_id=1)) | Q(price__gt=25))


    # 使用 F， 把所有书的价格增加 10
    books = Book.objects.all().update(price=F('price')+10.0)

    # 连表查询
    # 查询 publish表中的id = book表中出版社id的书
    books = Book.objects.filter(publiser_id=F('publiser__id'))



    for item in books:
        print(item.name)

    return HttpResponse('Success!')

from django.db.models import Max,Avg,Min,Count,Sum

def aggregate_function(request):
    '''
    聚合函数

    需要导入： from django.db.models import Max,Avg,Min,Count,Sum
    :return:
    '''

    # 查询所有书的平均价格
    ret = Book.objects.all().aggregate(Avg('price'))

    # 起别名 aggregate(priceAvg = Avg("price"))
    ret =  Book.objects.all().aggregate(priceAvg = Avg("price"))

    ret = Book.objects.all().aggregate(priceAvg = Avg("price"), priceMax = Max("price"), priceMin = Min("price"), priceSum = Sum("price"))

    print(ret)
    return HttpResponse('Success!')


def group_query(request):
    '''
    分组查询
    :param request:
    :return:
    '''

    return HttpResponse('Success!')


def printRes(ret):
    print(ret)
    for item in ret:
        # 循环出来的结果是unicode json字符串，需要转成 python对象
        dic = json.dumps(item, encoding='utf-8', ensure_ascii=False)
        print(dic)