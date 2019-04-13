# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def ajaxTest(request):
    return HttpResponse('1111111')