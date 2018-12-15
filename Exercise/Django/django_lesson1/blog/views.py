# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import time

# Create your views here.

def hello(request):
    return HttpResponse('你好，世界')

def showtime(request):
    return render(request, 'index.html', {'time':time.ctime()})

def artical(request, y, m):
    return HttpResponse('year: %s month: %s' % (y, m))

def artical_year_month(request, year, month):
    return HttpResponse('year: %s month: %s' % (year, month))


def register(request):
    if request.method == 'POST':
        print(request.POST.get('uname'))
        print(request.POST.get('pwd'))
        print(request.POST.get('hobay'))
        return HttpResponse('SUCCESS!')

    return render(request, 'register.html')
