# -*- coding:utf-8 -*-
'''

    Scrapy默认是不能在IDE中运行的，
    所以我们使用 scrapy 中的 cmdline 模块来执行 cmd 命令， 运行 spider 程序（其实就是模拟在命令行下运行 spider）


'''
from scrapy.cmdline import execute

# scrapy crawl itcastSpider (运行爬虫程序)
# scrapy crawl itcastSpider -o itcast.json/csv/xml （把数据导出到 itcast.json/csv/xml 文件）

# 前两个参数是不变的，第三个参是爬虫名称（spiders/mySpider.py 中的 name 属性值 itcastSpider）


# 直接运行 爬虫
# execute(['scrapy', 'crawl', 'itcastSpider'])

# 运行爬虫 并 写入到文件中
# execute(['scrapy', 'crawl', 'itcastSpider', '-o', 'itcast.csv'])

execute(['scrapy', 'crawl', 'tencentSpider'])
