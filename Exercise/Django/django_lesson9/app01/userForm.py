# -*- coding:utf-8 -*-

from django.forms import Form
from django.forms import fields, widgets
from django import forms

from app01.models import userInfo

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

    users1 = fields.ChoiceField(choices=((1, '大郎'),(2,'武松')))

    users2 = fields.ChoiceField(choices=[(1, '洪吉'),(2, '小东北')])


    '''
        生成动态的select：
        
            form中可以再前端生成select，select一般会分为两类:
                                                    
                                                    1、内容不变的数据。 
                                                    2、从数据库或者文件中提取的经常发生改变的数据。
                                                    
            如果从数据库提取数据，内容为免会经常发生增删改的情况，如果在使用1的实现方法就很不现实，
            此时我们就需要一种可以实现动态select的方法了。
            
            
            
            ChoiceField 中的 choices 的值 是元组列表 ：
                                                    ((1, '大郎'),(2,'武松')) 格式 
                                                     或者 
                                                     [(1, '洪吉'),(2, '小东北')] 格式
                                                     
            使用 all() 查询返回的是 [obj,obj,obj] ,列表中是一个个的对象，不符合要求
            使用 values() 查询返回的是 [{ },{ },{ }], 列表中是一个个的字典，也不符合要求
            使用 values_list() 查询返回的是 [( ),( ),( )] 列表中是一个个的元组，这个数据类型才符合要求，
            所以，必须使用 values_list() 方式
        
        
            问题： 
                
                ChoiceField 中的 choices 的值不能实时更新，在数据表更新时，不能实时的在页面中更新显示数据
                
            原因：
            
                这个不属于django的知识点，属于python面向对象的内容。
                python的类中可以定义静态字段，静态字段在类中加载后，被放入到内存中，如果再次修改静态字段，内存中的数据就不会在改变。
              
              静态字段：
              
                静态字段是属于类的。
                类中的静态字段会被加载放入到内存中，属于类里面的内容，在第一次运行程序的时候，
                只加载了一次。而我们每一次创建类的对象时，默认会执行类下面的 __init__构造函数。
                而静态字段属于类，不属于对象，所以之后的每一次访问时都不会再次加载类中的内容。
                所以当我们修改文件中或者数据库中与静态字段有关联的数据内容后，
                再次访问的时候，并不会修改内存中的数据。（除非我们把程序重启）
                
            
            解决：
            
                通过类的继承关系我们知道，如果执行的方法在当前类下没有，就会自动去父类中查找，如果有就会执行。
                我们可以在定义的form类下重定义__init__方法。
    '''
    # us = userInfo.objects.all().values_list('id','uname')
    # print(us)
    users3 = fields.ChoiceField()

    fileinput = fields.FileField()

    '''
        第一句中的super：执行父类中的__init__方法

        第二句这行代码什么意思呢，可以往父类中查找源码到底做了什么
        
        查找父类中的__init__方法，可以看到self.fields = copy.deepcopy(self.base_fields)，
        
        这一句就是把form类下面的静态字段都深copy了一份放在了对象里。这样，我们只需要修改对象里面那份数据就可以了。而类下面的数据不需要改变。
        
        self.fields的结果是一个字典，用['users3']就可以查找到在form类中定义的静态字段：users3 = forms.ChoiceField()
        
        通过.widget.choices 的方法就可以修改静态字段中的参数了。
        
        当前台页面再次访问时，就会拿到一份新的数据，生成了一个新元组，重新传到前端的html页面中。这样就实现了动态的 select。
    '''

    def __init__(self, *args, **kwargs):

        super(myform, self).__init__(*args, **kwargs)

        self.fields['users3'].widget.choices =  userInfo.objects.all().values_list('id','uname')

from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class ajaxform(forms.Form):
    uname = fields.CharField(required=True,
                             label='用户名',
                             error_messages={
                                 'required': '用户名不能为空',
                                 'invalid': '用户名格式错误'
                             },
                             help_text='5-20个字符')
    upwd = fields.CharField(max_length=8, min_length=6, required=True,
                            label='密码', label_suffix='?')
    age = fields.IntegerField(max_value=120, min_value=0, required=True)
    email = fields.EmailField(required=True)


    '''
     form Filed只能对输入的值做正则验证， 如果需要验证 用户名是否已存在等问题，需要从表中查询，
     如果存在就添加报错信息， Form.is_valid(): 在做字段验证的时候预留了一个验证扩展，方法名是： clean_字段名，
     
     如： 
        uname = fields.CharField() 字段
         方法名就是：
         
         clean_uname()
    
    Form 在做完正则验证后会调用此方法做验证
    
        def clean_uname(self):
            u = self.cleaned_data['uname']
    
            if userInfo.objects.filter(uname=u).count():
                raise ValidationError('用户名已存在')
    
            return u
        
    '''


    '''
    
    当我们要一次检查多个字段的时候，比如：用户名和邮箱都不能重复，多个验证显示一个错误
    
    再用‘clean_用户名()’这种方式一个字段一个字段的验证是不行的
    
    这时候可以用 Form 预留出来的 clean() 方法
    
    '''
    def clean(self):
        u = self.cleaned_data['uname']
        e = self.cleaned_data['email']

        if userInfo.objects.filter(uname=u).count() or userInfo.objects.filter(email=e).count():
            raise ValidationError('用户信息输入错误')

        return self.cleaned_data




