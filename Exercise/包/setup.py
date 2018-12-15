# -*- coding:utf-8 -*-
'''

setup(name = '压缩包名称', version = '1.0',
      description = '描述', author = '作者', py_moudles = ['',''] )

'''
from distutils.core import setup
setup(name = 'my_pub', version = '1.0',
      description = '描述', author = '作者',
      py_modules = ['MyPackage.module1','MyPackage.module2'])