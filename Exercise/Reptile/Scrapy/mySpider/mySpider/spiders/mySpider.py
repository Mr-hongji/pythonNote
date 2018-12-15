#coding:cp936

# 导入 Scrapy 包
import scrapy

# 自己定义的，需要保存的的字段
# 导入 mySpider 项目里 items文件中的 itcastSpiderItem 类
from ..items import itcastSpiderItem, tencentSpiderItem

# 导入 Scrapy 中的 Reuest 模块
from scrapy.http import  Request

'''

items 练习: class itcast (爬取传智播客教师信息)

PipeLines 练习: class tencent (爬取腾讯招聘信息)
 
'''

class itcast(scrapy.Spider):

    '''

        Itemss 练习

        爬取传智播客的老师数据（姓名、职称、简介）

        自定义爬虫类，继承 scrapy.Spider
        爬取 itcast.cn 中讲师的信息

    '''

    # 爬虫名
    name = 'itcastSpider'

    # 允许爬虫爬取的域
    allowed_domains = ['itcast.cn']

    # 爬取的url列表，爬虫在启动时会检测有没有 start_urls 这个属性
    # 然后从这个列表中取url 进行爬取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#apython']

    # 爬虫返回数据的回调方法, 这个方法是爬虫类必须写的
    def parse(self, response):

        teacher_items = []

        # 使用 scrapy中自带的 xpath 匹配获取的数据
        teachers =  response.xpath("//div[@class='li_txt']")

        for teacher in teachers:

            # item
            item = itcastSpiderItem()

            # 获取名称
            name = teacher.xpath('.//h3/text()').extract()
            # 获取职称
            title = teacher.xpath('.//h4/text()').extract()
            # 获取简介
            synopsis = teacher.xpath('.//p/text()').extract()

            # UnicodeEncodeError: 'gbk' codec can't encode character u'\xa0' in position 9 错误
            # 解决办法一： 在对unicode字符编码时，添加ignore参数，忽略无法无法编码的字符，这样就可以正常编码为GBK了
            item['name'] = name[0].encode("gbk", 'ignore')
            item['title'] = title[0].encode("gbk", 'ignore')
            item['synopsis'] = synopsis[0].encode("gbk", 'ignore')


            # 解决办法二： 替换掉u'\xa0'
            # item['name'] = name[0].replace(u'\xa0', u' ').encode("gbk")
            # item['title'] = title[0].replace(u'\xa0', u' ').encode("gbk")
            # item['info'] = info[0].replace(u'\xa0', u' ').encode("gbk")

            teacher_items.append(item)

        # 要使用 items 把数据保存到文件中，需要 return 数据
        # 返回的数据使用 start.py 文件中的exect 执行命令 ：
        # scrapy scrawl itcast -o itcast.jsom 把数据输出到 itcast.json 文件中
        return teacher_items



class tencent(scrapy.Spider):

    '''

        PipeLines 练习 爬取腾讯招聘信息

    '''
    name = 'tencentSpider'

    allowed_domains = ['tencent.com']

    url = 'https://hr.tencent.com/position.php?start='

    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):
        print(response.body)
        # 获取职位信息列表数据
        # 问题：在浏览器中使用 xpath help 工具 对 tbody 可以匹配数据， 在代码中使用 xpath 就匹配不出数据 如： //tbody/tr[@class='even']| //tbody/tr[@class='odd']
        # 答案：浏览器会在table标签下添加tbody（注：在chrome、火狐测试都有这个情况。出现这种原因是因为浏览器会对html文本进行一定的规范化 ）
        position_list = response.xpath("//tr[@class='even']| //tr[@class='odd']")

        for position in position_list:

            item = tencentSpiderItem()

            position_name = position.xpath('.//td[1]/a/text()').extract()
            position_category = position.xpath('.//td[2]/text()').extract()
            number = position.xpath('.//td[3]/text()').extract()
            locale = position.xpath('.//td[3]/text()').extract()
            release_time = position.xpath('.//td[5]/text()').extract()

            # print(position_name[0])
            # print(position_category[0])
            # print(number[0])
            # print(locale[0])
            # print(release_time[0])

            if len(position_name) > 0:
                item['position_name'] = position_name[0]

            if len(position_category) > 0:
                item['position_category'] = position_category[0]

            if len(number) > 0:
                item['number'] = number[0]

            if len(locale) > 0:
                item['locale'] = locale[0]

            if len(release_time) > 0:
                item['release_time'] = release_time[0]

            # 使用 yield 返回的数据会经过 pipelines
            yield item

            # 使用return 数据不会经过 pipelines
            # return item

        if self.offset < 349:
            self.offset += 1

        yield  scrapy.Request(self.url + str(self.offset), callback=self.parse)
