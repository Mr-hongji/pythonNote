# -*- coding:utf-8 -*-

"""django_lesson1 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from blog.views import hello,showtime,artical_year_month,register,artical

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^hello/$', hello),

    url(r'^showtime/$', showtime),

    url(r'^artical/(\d{4})/(\d{2})$', artical),

    # 使用别名的方式后，views的处理函数中的参数名必须是 此处使用的别名
    url(r'^artical/(?P<year>\d{4})/(?P<month>\d{2})$', artical_year_month),

    url(r'^blog/', include('blog.urls'))

]
