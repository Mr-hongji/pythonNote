# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse

from app01.models import Students, Classes


def students(request):
    stu_list = Students.objects.all()
    return render(request, 'students.html',locals())

def add_student(request):
    cls_list = Classes.objects.all()
    return render(request, 'add_student.html', locals())

def addstudent(request):
    if request.method == 'POST':
        sname = request.POST.get("sname")
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        cls = request.POST.get('cls')
        Students.objects.create(name=sname, gender=gender, age=age, c_id=cls)

    return redirect('students.html')

def deleteStudent(request):
    sid = request.GET.get('sid')
    Students.objects.filter(id=sid).delete()
    return redirect('students.html')


def update_Student(request):
    sid = request.GET.get('sid')
    stu = Students.objects.filter(id = sid).first()
    cls_list =Classes.objects.all()
    return render(request, 'update_Student.html', locals())

def updateStudent(request):
    sid = request.GET.get('sid')
    sname = request.POST.get("sname")
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    cls = request.POST.get('cls')
    Students.objects.filter(id=sid).update(name=sname, gender=gender, age=age, c_id=cls)
    return redirect('students.html')

def ajaxDeleteStudent(request):
    try:
        uid = request.POST.get('id')
        print(uid)
        Students.objects.filter(id=uid).delete()
        r = 1
    except Exception as e:
        r = -1

    res = '{"resultMsg":'+str(r)+'}'
    return HttpResponse(res)