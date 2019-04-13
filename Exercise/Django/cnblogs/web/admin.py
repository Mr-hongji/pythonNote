# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from web import models
# Register your models here.

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


admin.site.register(models.User)
admin.site.register(models.Blog)
admin.site.register(models.BlogCategory)
admin.site.register(models.WebSitesClassificationLeval)

admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.UpDown)
admin.site.register(models.Comment)
admin.site.register(models.ReportingObstacles)

