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
    f = myform()
    return render(request, 'adduser.html', locals())

def add_user(request):
    '''
    使用普通方式添加 userinfo， 没有做输入验证
    :param request:
    :return:


    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    age = request.POST.get('age')
    email = request.POST.get('email')
    userInfo.objects.create(uname=uname, upwd=upwd, age=age, email=email)

    return redirect('users.html')

    '''
    '''
        使用 form 做输入验证

        :param request:
        :return:
        '''

    f = myform(request.POST)

    if f.is_valid():
        userInfo.objects.create(**f.cleaned_data)
        return redirect('users.html')
    else:
        return render(request, 'adduser.html', {'f': f})


from django.forms import Form
from django.forms import fields, widgets

class myform(Form):
    uname = fields.CharField(max_length=20,
                             min_length=5,
                             required=True,
                             label='用户名',
                             error_messages={
                                 'max_length':'用户名为 5-20个字符',
                                 'min_length': '用户名为 5-20个字符',
                                 'required': '用户名不能为空',
                                 'invalid':'用户名格式错误'
                             })
    upwd = fields.CharField(max_length=8, min_length=6, required=True)
    age = fields.IntegerField(max_value=120, min_value=0, required=True)
    email = fields.EmailField(required=True)
    gender = fields.CharField(
            initial=2,
            widget=widgets.RadioSelect(choices=((1,'上海'),(2,'北京'),))
        )
    fileinput = fields.FileField()
