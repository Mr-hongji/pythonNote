# -*- coding:utf-8 -*-
from app01.models import Teachers
from django.shortcuts import render, redirect

def teschers(req):
    teacher_list = Teachers.objects.all()
    return render(req, 'teachers.html', locals())

def addteacher(request):
    name = request.POST.get('teachername')
    Teachers.objects.create(name=name)

    return  redirect('teachers.html')

def addtescherpage(request):
    return render(request, 'addTeacher.html')