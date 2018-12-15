# -*- coding:utf-8 -*-
''''''
'''
协程

    * 比线程更小的执行单元
    * 在一个线程中可以包含多个协程
    * 协程的切换只是单纯的操作CPU上下文，比线程的切换更快速


特点：

    * 消耗的内存资源少
    
    
使用场合：IO密集型程序

    * 程序一般分两种：
    
        - IO密集型程序：经常需要访问网络或去磁盘上读写文件
            
        - CPU密集型程序

    

同进程和线程区别：

    * 进程和线程，系统控制它们的切换 ---  协程是用户自己去切换
    

实现协程的方式：
    
        * 使用生成器 yield
        
            - 代码复杂的时候，手动切换的话，操作起来会很麻烦
            
        * 使用 greenlet 第三方模块
        * 使用 gevent 第三方模块


        greenlet、gevent模块安装：
        
            * 模块下载地址：https://pypi.org/project/greenlet/#files
            
            * 模块安装：
               - 打开cmd
               - 运行 pip install greenlet==0.3 和  pip install gevent==1.2 （支持 python 2.7.9）    
            
            * 可能出现错误：
            
               - error: Microsoft Visual C++ 9.0 is required (Unable to find vcvarsall.bat). Get it from http://aka.ms/vcpython27
                   （解决：去http://aka.ms/vcpython27 下载安装 VCForPython27.msi 即可）
            
               - whl is not a supported wheel on this platform.
                        （说明安装的模块版本和使用的python版本不对）
            
            * 安装成功提示：
                Successfully installed gevent greenlet
                Cleaning up...


'''