# -*- coding:utf-8 -*-
''''''
'''
    Python 默认自带库：
    
        * urllib、re
        
    需要安装的库：
        
        * requests
            
            - 安装
                。pip3 install requests
            - 测试
                。import requests
                。requests.get('http://www.baidu.com')
                
        * selenium
            
            - 驱动浏览器的库、做自动测试的
            - 在做爬虫时，会遇到一些 JS 渲染的页面，requests 不能正常获取请求的内容
            - 使用这个库可以直接驱动浏览器，用浏览器来执行 JS 渲染，就可以拿到 JS 渲染之后的页面内容
            - 安装
                。 pip3 install selenium
            - 安装完成验证
                。from selenium import webdriver
                。driver = webdriver.Chrome()
                
            - 执行后可能会遇到的错误：
            
               。Traceback (most recent call last):
                File "<stdin>", line 1, in <module>
                File "D:\ProgramFiles\Python3\lib\site-packages\selenium\webdriver\chrome\webd
                river.py", line 68, in __init__
                self.service.start()
                File "D:\ProgramFiles\Python3\lib\site-packages\selenium\webdriver\common\serv
                ice.py", line 83, in start
                os.path.basename(self.path), self.start_error_message)
                selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executabl
                e needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chrome
                driver/home
                
                。原因：没有安装 Chrome 浏览器驱动
                
                。Chrome 浏览器驱动
                    
                    ` 安装 ChromeDriver
                    ` 下载地址：http://chromedriver.chromium.org/
                    ` 解压后，把 exe 文件放到 python安装目录下 或者 安装目录下的 Script 目录
                    
                    ` 重新启动 CMD 运行 chromedriver,显示：Starting ChromeDriver 2.40.565498 port 9515...
                    
                    ` 重新运行 ‘ 模块安装完成验证的代码 ’，正常会启动 Chrome 浏览器
                    
                    ` 然后执行：
                        driver.get('http://www.baidu.com'),启动的浏览器会访问百度页面
                
                。phantomjs
                
                    ` 是一个无界面浏览器驱动，在爬虫时就不会弹出浏览器，会在后台静默运行
                    
                    ` 安装：
                        ·下载地址：http://phantomjs.org/download.html
                        ·下载后解压，把解压目录拷贝到自己的位置然后配置环境变量 
                            ` 比如我的：PATH: D:\ProgramFiles\phantomjs-2.1.1-windows\bin
                        
                        ·重新打开 CMD 运行 phantomjs，在里面可以直接运行 JS 代码：
                            ` comsole.log('Hello World')    
                            
                        ·‘Ctrl C’退出
                        
                        · 执行：
                            
                            from selenium import webdriver
                            driver = webdriver.phantomjs()
                            访问百度页面：driver.get('http://www.baidu.com')
                            打印页面信息：driver.page_source 
                            
            * lxml
            
                - 提供了 xpath 数据解析方式
                
                - 安装：pip3 install lxml
                
            
            * beautifulsoup
            
                - 网页解析库，依赖于 lxml 库，安装前需先安装lxml
                
                - 安装：pip3 install beautifulsoup4 (是beautifulsoup的第四个版本)
                    
                - 执行 
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup('<html></html>','lxml')
                
                - BeautifulSoup(参数一：网页源代码，参数二：数据解析方式)
                
            
'''

