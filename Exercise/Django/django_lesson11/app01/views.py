# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

def index(request):
    return render(request, 'index.html')

def sendata(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse('哎呀！我去')

import os

def uploadfile(request):
     print(request.GET)
     print(request.POST)
     print(request.FILES.get('img'))
     img = request.FILES.get('img')

     imgpath = os.path.join('static', img.name)
     f = open(imgpath, 'wb')
     for line in img.chunks():
         f.write(line)
     f.close()

     return HttpResponse(imgpath)