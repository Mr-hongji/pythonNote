"""django_lesson6 URL Configuration

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

from app01.views.classes import  classes, add_class, addclass, dispatchteacherpage,\
    dispatchteacher, ajaxAddClass, ajax_addclass
from app01.views.students import add_student, students, addstudent, deleteStudent,\
    update_Student, updateStudent, ajaxDeleteStudent

from app01.views.teachers import teschers,addteacher,addtescherpage

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^classes.html$', classes),
    url(r'^add_class.html$', add_class),
    url(r'^addclass$', addclass),
    url(r'^dispatchteacher.html$', dispatchteacherpage),
    url(r'^dispatchteacher$', dispatchteacher),
    url(r'^ajaxAddClass.html$', ajaxAddClass),
    url(r'^ajax_addclass$', ajax_addclass),

    url(r'^add_student.html$', add_student),
    url(r'^students.html$', students),
    url(r'^addstudent$', addstudent),
    url(r'^deleteStudent.html$', deleteStudent),
    url(r'^update_Student.html$', update_Student),
    url(r'^updateStudent$', updateStudent),
    url(r'^ajaxDeleteStudent$', ajaxDeleteStudent),

    url(r'^teachers.html$', teschers),
    url(r'^addteacher$', addteacher),
    url(r'^addteacher.html$', addtescherpage),

]
