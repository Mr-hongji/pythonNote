# -*- coding:utf-8 -*-

from django.forms import Form
from django.forms import fields, widgets
from django import forms

class myform(Form):
    uname = fields.CharField(max_length=20,
                             min_length=5,
                             required=True,
                             label='用户名',
                             error_messages={
                                 'max_length':'用户名为 5-20个字符',
                                 'min_length': '用户名为 5-20个字符',
                                 'required': '用户名不能为空',
                                 'invalid':'用户名格式错误'
                             },
                             help_text='5-20个字符')
    upwd = fields.CharField(max_length=8, min_length=6, required=True,
                            label='密码', label_suffix='?')
    age = fields.IntegerField(max_value=120, min_value=0, required=True)
    email = fields.EmailField(required=True)

    gender = fields.CharField(
            initial=1, # 设置初始化时的默认值
            widget=widgets.RadioSelect(choices=((1,'男'),(2,'女'),))
        )

    getMarried = fields.CharField(
        initial=1,
        widget=forms.RadioSelect(choices=((1, '是'),(2, '否'))))


    fileinput = fields.FileField()