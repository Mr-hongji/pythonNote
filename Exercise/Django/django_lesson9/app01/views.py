# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from models import userInfo

# Create your views here.
def users(request):
    user_list = userInfo.objects.all()
    return render(request, 'users.html', locals())

def adduserpage(request):
    return render(request, 'adduser.html')

def add_user(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    age = request.POST.get('age')
    email = request.POST.get('email')
    userInfo.objects.create(uname=uname, upwd=upwd, age=age, email=email)

    return redirect('users.html')
