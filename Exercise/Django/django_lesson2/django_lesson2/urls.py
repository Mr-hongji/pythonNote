"""django_lesson2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls import url,include
from app01.views import statics_param,\
    use_locals, register, login, filter_use, student_page,base_page, fbv, cbv

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^statics$', statics_param),
    url(r'^useLocals$', use_locals),
    url(r'^login$', login, name='login'),
    url(r'^register$', register),
    url(r'^filter_use$', filter_use),
    url(r'^base$', base_page),
    url(r'^student$', student_page),


    url(r'^FBV$', fbv),
    url(r'^CBV$', cbv.as_view())
]
