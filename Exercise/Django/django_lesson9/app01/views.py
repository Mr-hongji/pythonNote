# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from models import userInfo

from userForm import myform, ajaxform

# Create your views here.
def users(request):
    user_list = userInfo.objects.all()
    return render(request, 'users.html', locals())


'''
    auto_id：
    
        生成的HTML元素中是否带有 id 属性
        
        值:
            True（带id属性） | False（不带id属性） | 'id_%s'（带id属性，id格式是：id_元素的name名）

    label_suffix：

        也可以在创建Field 的时候设置，如：
        fields.CharField(label='密码', label_suffix='? ')
        这样就会覆盖在     f = myform(auto_id=False, label_suffix=':') 时所设置 label_suffix
'''

def adduserpage(request):

    f = myform(auto_id='id_%s', label_suffix=':')

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

        上传文件时需要给 form 对象传 files=request.FILES 参数
        
    '''

    f = myform(request.POST, auto_id=False, files=request.FILES)

    if f.is_valid():
        userInfo.objects.create(**f.cleaned_data)
        return redirect('users.html')
    else:
        return render(request, 'adduser.html', {'f': f})


import json
from django.forms.utils import ErrorDict

def adduser_ajax(request):

    ret = {'status':False, 'message':None}

    if request.method == 'GET':
        f  = ajaxform()
        return  render(request, 'adduser_ajax.html', {'f': f})
    else:
        f = ajaxform(request.POST)
        if f.is_valid():
            ret['status'] = True
        else:

            print(type(f.errors))

            '''
                 打印发现f.errors 是一个django.forms.utils.ErrorDict 类型, 
                 导入  from django.forms.utils import ErrorDict，进入 ErrorDict 的源码发现，
                 ErrorDict 继承自 Dict, 而且还有 as_data(), as_json(), as_ul(), as_text() 这几个可以转换数据格式
                 的方法
            
            '''
            # print(f.errors.as_ul())
            # print(f.errors.as_data())
            # print(f.errors.as_json())
            # print(f.errors.as_text())



            ret['message'] = f.errors

        ret = json.dumps(ret)
        print(ret)
        return HttpResponse(ret)


