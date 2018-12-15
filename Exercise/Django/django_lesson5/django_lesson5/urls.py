# -*- coding:utf-8 -*-
"""django_lesson5 URL Configuration

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

from django.conf.urls import url
from django.contrib import admin
from app01.views import one_to_maney, many_to_many, q_f, aggregate_function, group_query

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 一对多
    url(r'^one_to_many$', one_to_maney),

    # 多对多
    url(r'^many_to_many$', many_to_many),

    # 使用 Q 和 F
    url(r'^q_f$', q_f),

    #聚合函数
    url(r'^aggregate_function$', aggregate_function),

    #分组查询
    url(r'^group_query$', group_query),
]
