# -*- coding:utf-8 -*-

'''

自定义过滤器

    1、在应用目录下 新建 templatetags 目录，然后新建一个 py 文件
    2、导入：
        from django import template

        register = template.Library()

    3、在使用过滤器的 html 中加载过滤器 py 文件
        {% load mytag %}

filter 只能穿两个参数：{{ age|multi:2 }}（age 是第一个参数， 2 是第二个参数）

详细看文档：https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/#django.template.Library.filter
'''

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def multi(arg1, arg2):
    return arg1 * arg2


@register.filter
def add_1(arg1, arg2):
    n = 0
    for i in arg2:
        n += i
    return arg1 + n



@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<strong>%s</strong>%s' % (esc(first), esc(other))
    return mark_safe(result)



'''

自定义标签

    和自定义过滤器实现的效果一样，使用方法不一样
'''

@register.simple_tag
def simple_tag_multi(arg1, arg2, arg3):
    return arg1 * arg2 * arg3
