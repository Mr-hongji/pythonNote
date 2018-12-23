# -*-coding:utf-8-*-
from django.shortcuts import HttpResponse, render, redirect
import json

from app01.models import Students, Classes

def students(request):
    stu_list = Students.objects.all()
    cls_list = Classes.objects.all()
    return render(request, 'Students.html', locals())

def addStudent(request):
    res = {'status':False, 'msg':None}

    try:
        name = request.POST.get('stuName')
        age = request.POST.get('stuAge')
        gender = request.POST.get('stuGender')
        cls = request.POST.get('stuCls')

        if gender == 'false':
            gender = False
        else:
            gender = True

        stu = Students.objects.create(name=name, age=age, gender=gender, c_id=cls)
        print(name)
        res['status'] = True

        res['stuid'] = stu.id

    except Exception as e:
        res['msg'] = '输入错误'

    resdata = json.dumps(res, ensure_ascii=False)
    print(resdata)
    return HttpResponse(resdata)


def delStudent(request):
    res = {'status':False, 'msg':None}

    try:
        id = request.POST.get('id')
        Students.objects.filter(id=id).delete()
        res['status'] = True
    except Exception as e:
        res['msg'] = '数据删除失败'

    resdata = json.dumps(res, ensure_ascii=False)
    return HttpResponse(resdata)