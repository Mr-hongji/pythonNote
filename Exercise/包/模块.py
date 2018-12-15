# -*- coding:utf-8 -*-
''''''

'''

模块导入方式：

    * import
        
        * 语法： import 模块1，模块2...
        * 使用： 模块名.函数名
        * 例如使用 math 模块：
            - import math （导入模块）
            - print math.ssqrt(2) （使用）
            
            
    * from ... import ...
    
        * 语法： from 模块1，模块2 import (函数名，类名，或属性名) 
        * 使用： 函数名()、属性名、类名.函数名()
        * 例：
            - from math import sqrt
            _ print sqrt(2)
            
            
    
    * from ... import *
        
        * 此方式不提倡使用（违背python原则）
        * 容易导致的问题：   
            1、当两个模块 moudle1 和 moudle2,中都存在 test()
            函数，使用这种导入方式时，后面导入的会覆盖前面导入的
            
            from moudle1 import *
            from moudle2 import *
            
            print(test()) 此时，会调用moudle中的 test() 函数
            
as:

    * 当模块名或者函数名特别长时可以使用 as 创建别名
    * 例：
        - from random as rm
        - print(rm.randint(1,9))



'''