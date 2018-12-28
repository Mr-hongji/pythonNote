# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import math

# Create your views here.
from django.core import paginator
items = []

for i in range(1, 999):
    items.append('Item_' + str(i))

def index(request):
    page = int(request.GET.get('page'))

    if len(items) % 10 > 0:
        pageCount = (len(items) / 10) + 1
    else:
        pageCount = len(items) / 10

    # 1  1 - 10 [(page - 1) * 10, page * 10]
    # 2 11 - 20
    # 3 21 - 30
    pre_page = page - 1
    if pre_page < 1:
        pre_page = 1

    next_page = page + 1
    if next_page > pageCount:
        next_page = pageCount

    print(page)

    page_nums = []
    for num in range(1,6):
        if(page - num > 0):
            page_nums.append(page - num)

    page_nums.reverse()

    page_nums.append(page)

    for num in range(1, 11 - len(page_nums)):
        if page + num <= pageCount:
            page_nums.append(page + num)



    item_list = items[(page - 1) * 10: page * 10]
    print(item_list)
    return render(request, 'index.html', {'itemList': item_list,
                                          'pre_page': pre_page, 'next_page':
                                              next_page, 'page_nums': page_nums, 'pageCount':pageCount,
                                          'current_page':page})

from paginator import paginator
def pages(request):

    page_size = 11 # 每页显示条数

    current_page = int(request.GET.get('page'))

    page = paginator(current_page, len(items), page_size)

    item_list = items[(page.current_page - 1) * page_size: page.current_page * page_size]

    print(item_list)
    # return render(request, 'index.html',{'itemList': item_list, 'pre_page': page.prePage, 'next_page': page.nextPage, 'page_nums': page.pageNum, 'pageCount': page.pageCount, 'current_page': current_page})
    return render(request, 'paginator.html', {'itemList': item_list,
                                              'paginatorResult': page.paginatorResult,
                                              'paginatorResult_BootStrap':page.paginatorResult_BootStrap})
