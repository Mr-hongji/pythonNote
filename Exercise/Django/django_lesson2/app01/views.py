from django.shortcuts import render, redirect, HttpResponse
from django.utils.safestring import mark_safe

# Create your views here.

def statics_param(request):
    content = {}

    content['name'] = '大王'
    content['age'] = 20
    content['sex'] = '公'

    return render(request, 'index.html', content)

'''
locals() 的使用

return render(request, 'index.html', locals())

'''
def use_locals(request):
    name = '小王'
    age = 15
    sex = '公'

    hobby = ['吃', '喝', '扯犊子', '看片']
    book={'name':'论扯犊子'}

    return render(request, 'index.html', locals())


def login(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')
    return render(request, 'login.html', locals())


'''
redirect（）重定向方法的使用

redirect('login.html',{'uname':uname, 'pwd':pwd})

'''

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        return redirect('login.html',{'uname':uname, 'pwd':pwd})

    return render(request, 'register.html')

def filter_use(request):
    name = 'oldK'
    age = 20
    sex = '公'
    atag = '<a href="">点一下</a>'
    safetag = mark_safe("<a href='{%url equip:listEquipmentCategory 1 %}'>首页</a>")
    hobby = ['吃', '喝', '扯犊子', '看片']
    hobby = []
    l = [1, 1, 1, 1, 1]
    return render(request, 'filter_use.html', locals())


def base_page(request):
    return render(request, 'base.html')


def student_page(request):
    return render(request, 'student.html')

def fbv(request):
    return  HttpResponse('FBV')

from django.views import View
class cbv(View):
    def get(self, request):
        return render(request, 'CBV.html', {'method':'CBV.GET'})

    def post(self, request):
        return render(request, 'CBV.html', {'method': 'CBV.POST'})

