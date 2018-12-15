# -*- coding:utf-8 -*-

# 使用 render 来替代 pro1 中使用的 HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World!' # 键值 "hello" 对应模板中的变量 "{{ hello }}"
    return render(request, 'hello.html', context) # 向模板提交数据


def hello_extends_base(request):
    context = {}
    context['hello'] = 'Hello World!' # 键值 "hello" 对应模板中的变量 "{{ hello }}"
    return render(request, 'hello_extends_base.html', context) # 向模板提交数据
