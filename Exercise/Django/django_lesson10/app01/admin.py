# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app01.models import User, Hobby, UserToHobby


'''
Django——报错：admin后台添加中文数据时报错:

        UnicodeEncodeError: 'ascii' codec can't encode characters in position..
        
解决： 在app下的admin.py 文件中添加：

import sys;
reload(sys);
sys.setdefaultencoding("utf8")


'''
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

# Register your models here.
admin.site.register(User)
admin.site.register(Hobby)
admin.site.register(UserToHobby)
