# -*- coding:utf-8 -*-
"""django_pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

'''

url(regex, view, kwargs=None, name=None)：

    参数：
        两个必选参数：regex、view 
        两个可选参数：kwargs、name

    regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。

    view: 用于执行与正则表达式匹配的 URL 请求。

    kwargs: 视图使用的字典类型的参数。

    name: 用来反向获取 URL。
    

Django 版本 >= 2.0：

    from django.conf.urls import url 被 from django.urls import path 取代。
    使用 urlpatterns = [ path('world/', view.world)]， 路径后要加 '/'
    
'''

from django.conf.urls import url
from django.contrib import admin
from view import hello

urlpatterns = [
    url(r'^$', hello),
    url(r'^hello/$', hello)
]
