# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

from django.shortcuts import HttpResponse

from django.forms import Form, fields

class userForm(Form):
    uname = fields.CharField()
    imageFile = fields.FileField()

def adduser(request):
    if request.method == 'GET':
        f = userForm()
        return render(request, 'adduser.html', {'f':f})

    else:
        imgFile = request.FILES.get('imageFile')


        wf = open(imgFile.name, 'wb')

        for line in imgFile.chunks():
            wf.write(line)

        wf.close()

        return HttpResponse('OK')


from app01.models import UserToHobby

def getuser(request):
    UserToHobby.objects.all().select_related()
    UserToHobby.objects.all().prefetch_related()

    return HttpResponse('ok')