# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
from app01.models import Classes, Teachers

def index_html(request):
    return render(request, "students.html")

def add_class(request):
    return render(request, 'add_class.html')

def addclass(request):
    if request.method == "POST":
        classname = request.POST.get("classname")
        Classes.objects.create(name=classname)

    cls_list = Classes.objects.all()
    return redirect('classes.html', {'classes_list': cls_list})

def classes(request):
    cls_list = Classes.objects.all()

    return render(request, 'classes.html', locals())

def dispatchteacherpage(request):
    classid = request.GET.get('classid')
    teacher_list = Teachers.objects.all()
    cls = Classes.objects.filter(id=classid).first()
    cls_teachets = cls.teacher.all()
    return render(request, 'dispatcherTeacher.html', locals())

def dispatchteacher(request):
    teachers = request.POST.getlist('teachers')
    print(teachers)
    classid = request.GET.get('classid')
    print(classid)
    cls = Classes.objects.filter(id=classid).first()
    print(cls)
    cls.teacher.add(*teachers)
    cls.teacher.set(teachers)
    return redirect('classes.html')

def ajaxAddClass(request):
    return render(request, 'ajaxAddClass.html')

def ajax_addclass(request):
    clsname = request.POST.get('name')
    print(clsname)
    if(clsname == ''):
        return HttpResponse('班级名称不能为空')
    Classes.objects.create(name=clsname)
    return HttpResponse('success')