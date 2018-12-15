# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from app01.models import Book

# Create your views here.

def index(request):
    return render(request, 'index.html')

def addbook(request):

    # 方式一
    b = Book(name='Python', price=20, pub_date='2018-09-16', author='小王')
    b.save()

    # 方式二
    Book.objects.create(name='三重门', price=39.8, pub_date='2018-01-01', author='韩寒')

    return HttpResponse('添加成功')



def  updatebook(request):


    '''
    方法一和方法二的区别：

        get方法：
            1、从数据库的取得一个匹配的结果，返回一个对象。
            2、如果记录不存在 或 查询出两条以上的数据，它会报错。
            3、update() 方法只更新要更新的列， 效率更高
            4、save() 方法会更新所有列， 效率低

        filter方法：
                1、从数据库的取得匹配的结果，返回一个对象列表。
                2、如果记录不存在的话，它会返回[]。



    '''

    # 方式一 会同时修改多条数据
    # 翻译后的原生语句（只更新了一列）：
    # UPDATE `app01_book` SET `price` = 100 WHERE `app01_book`.`author` = '大王'; args=(100.0, u'\u5927\u738b')
    Book.objects.filter(author='大王').update(price=100)

    # 方式二
    # 翻译后的原生语句（更新了所有列）：
    #  UPDATE `app01_book` SET `name` = '文化苦旅', `price` = 12, `pub_date` = '2014-04-01', `author` = '雨果' WHERE `
    # app01_book`.`id` = 3; args=(u'\u6587\u5316\u82e6\u65c5', 12.0, u'2014-04-01', u'\u96e8\u679c', 3)
    b = Book.objects.get(author='雨果')
    print(b)
    b.price = 12
    b.save()

    return HttpResponse('修改成功')

def deletetbook(request):

    Book.objects.filter(author='韩寒').delete()

    return HttpResponse('删除成功')

def selectbook(request):

    # 查询所有记录
    book_list = Book.objects.all()

    # 使用切片查询前三条（也可以使用步长）
    # 使用切片，就是原生sql 中的 limit 如：
    # SELECT `app01_book`.`id`, `app01_book`.`name`, `app01_book`.`price`, `app01_book`.`pub_date`, `app01_book`.`author` FROM `app01_book` LIMIT 3;
    book_list = Book.objects.all()[:3]

    # 设置步长是 2
    book_list = Book.objects.all()[::2]

    # 条件查询

    # 使用 get 返回筛选条件相匹配的对象，返回结果只有一个，如果超过一个或者没有就会抛异常
    # 返回一个对象 不是 列表
    book_list = Book.objects.get(author='Bruce Eckel')

    # 获取第一条数据
    # 返回一个对象 不是列表
    book_list = Book.objects.first()

    # 获取最后一条数据
    # 返回一个对象 不是列表
    book_list = Book.objects.last()


    # 查询 author = '大王' 的书
    book_list = Book.objects.filter(author='大王')

    # 查询 author = '大王' 的书的名称和价格
    # values 和 values_list 区别是返回的数据格式不同
    book_list = Book.objects.filter(author='大王').values_list('name', 'price')
    print(book_list) # <QuerySet [(u'PHP', 100.0), (u'Python', 100.0)]>
    book_list = Book.objects.filter(author='大王').values('name', 'price')
    print(book_list) # <QuerySet [{u'price': 100.0, u'name': u'PHP'}, {u'price': 100.0, u'name': u'Python'}]>

    # 对查询结果排序 order_by()
    # 对查询结果反向排序 reverse()
    book_list = Book.objects.filter(author='大王').values('name', 'price').order_by('price')

    # 获取查询的数据条数 count()
    book_list = Book.objects.filter(author='大王').count()

    # 模糊查询——万能的双下划线 （使用双下划綫实现模糊查询）
    # 查询作者名字中含有 ‘王’ 的书
    book_list = Book.objects.filter(author__contains='王')

    # 判断返回的 QuerySet 是否有数据，有返回True, 没有返回False
    book_list.exists()

    # distinct() 查询结果去重
    # 按照 name, author 组合去除重复的内容
    book_list = Book.objects.filter(author__contains='王').values('name', 'author').distinct()

    # 按照 author 组合去除重复的内容
    book_list = Book.objects.filter(author__contains='王').values('author').distinct()

    return render(request, 'index.html', locals())
