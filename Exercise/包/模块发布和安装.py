# -*- coding:utf-8 -*-
''''''
'''

    发布自己的模块，并把模块安装到Python系统的目录中，
    这时任何项目都可以使用

    以 MyPackage 包为例：
    
       1、 MyPackage 下有两个模块 module1 和 module2 目录结构如下：
            
           .
            |___ 包             
                 |____ MyPackage 
                 |          |__ __init__.py
                 |          |__ module1.py
                 |          |__ module2.py
                 |
                 |__ setup.py
                
        2、在 MyPackage 的平级目录下新建 setup.py
        
            .
            |___ 包             
                 |____ MyPackage 
                 |          |__ __init__.py
                 |          |__ module1.py
                 |          |__ module2.py
                 |
                 |__ setup.py
            
        3、在 setup.py 文件中输入如下内容：
        
            from distutils.core import setup
            setup(name = 'my_pub', version = '1.0',
                description = '描述', author = '作者',
                py_modules = ['MyPackage.module1','MyPackage.module2'])
            
        4、构建模块，在 cmd 中 执行：
        
            python setup.py build
            
            执行完后，这时会生成一个 build 目录：
            
            .
            |___ 包             
                 |____ MyPackage 
                 |          |__ __init__.py
                 |          |__ module1.py
                 |          |__ module2.py
                 |
                 |__ setup.py
                 |
                 |__ build
                        |__ lib
                             |__ MyPackage
                                    |__ __init__.py
                                    |__ module1.py
                                    |__ module2.py
            
             
            5、生成发布压缩包，cmd 中执行:
                
                 python setup.py  sdist  
                 
                 执行后，会生成一个 dist 目录：  
                 
                 
                  .
                |___ 包             
                     |____ MyPackage 
                     |          |__ __init__.py
                     |          |__ module1.py
                     |          |__ module2.py
                     |
                     |__ setup.py
                     |
                     |__ build
                     |      |__ lib
                     |           |__ MyPackage
                     |                  |__ __init__.py
                     |                  |__ module1.py
                     |                  |__ module2.py
                     |__ dist
                            |__ my_pub-1.0.zip
                            
                            
                            
            6、找到发布的压缩包，解压
            7、进入解压后的目录
            8、安装模块，cmd 执行：
             
                python setup.py install  
                    
'''