# -*- coding:utf-8 -*-

from scrapy_redis.spiders import RedisSpider
import json, scrapy
from ..items import ZhilianzhaopinItem
import sys
import re, time
reload(sys)
sys.setdefaultencoding('utf8')
class zhilianSpider(RedisSpider):

    name = 'zhilian1'
    redis_key = 'zhilian1:start_urls'
    pageSize = 30
    start = 0
    url = 'https://fe-api.zhaopin.com/c/i/sou?cityId=530&sortType=&kw=python&kt=3&lastUrlQuery={"jl":"530","kw":"python","kt":"3"}'
    '''
    url = 'https://fe-api.zhaopin.com/c/i/sou?cityId=530&sortType=&kw=python&kt=3&lastUrlQuery={"jl":"530","kw":"python","kt":"3"}'
    pageSize：每页显示数据条数
    cityId: 城市id
    kw(key word): 搜索关键词
    kt（key type）：关键词类型 2：公司 | 3：职位
    lastUrlQuery = {"jl": "530", "kw": "python", "kt": "3"}: jl（job location）: 同 cityId
    sortType = '' 智能排序 | 'salary' 薪酬最高 | 'publish' 最新发布
    
    '''

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(zhilianSpider, self).__init__(*args, **kwargs)

    def parse(self, response):

        position_list = json.loads(response.body.encode('utf-8'))

        for position in position_list['data']['results']:
            position_url = position['positionURL']
            yield scrapy.Request(url=position_url, callback=self.parseJobData)

        self.start += self.pageSize


        rurl = self.url + '&pageSize=' + str(self.pageSize) + '&start=' + str(self.start)
        yield scrapy.Request(url=rurl, callback=self.parse)



    def parseJobData(self, response):

        item = ZhilianzhaopinItem()

        if len(response.xpath("//div[@class='inner-left fl']/h1/text()")) > 0:
            item['position_name'] = response.xpath("//div[@class='inner-left fl']/h1/text()").extract()[0].replace(u'\xa0', '').encode('utf-8').strip()

        item['work_place'] = response.xpath("//div[@class='terminalpage-main clearfix']//div[@class='tab-inner-cont'][1]//h2/text()").extract()[0].replace(u'\xa0', '').encode('utf-8').strip()
        item['working_seniority'] = response.xpath("//div[@class='terminalpage-left']/ul//strong/text()").extract()[3].replace(u'\xa0', '').encode('utf-8').strip()
        item['educational_requirements'] = response.xpath("//div[@class='terminalpage-left']/ul//strong/text()").extract()[4].replace(u'\xa0', '').encode('utf-8').strip()
        item['salary'] = response.xpath("//div[@class='terminalpage-left']/ul//strong/text()").extract()[0].replace(u'\xa0', '').encode('utf-8').strip()
        item['position_information'] = self.getPositionInformation(response)
        item['position_welfare'] = ' '.join(response.xpath("//div[@class='welfare-tab-box']//span/text()").extract()).replace(u'\xa0', '').encode('utf-8').strip()
        item['company_name'] = response.xpath("//div[@class='company-box']//a/text()").extract()[0].replace(u'\xa0', '').encode('utf-8').strip()
        item['company_industry'] = response.xpath("//div[@class='company-box']//li//a/text()").extract()[0].replace(u'\xa0', '').encode('utf-8').strip()
        item['company_nature'] = response.xpath("//div[@class='company-box']/ul/li[2]//strong/text()").extract()[0].replace(u'\xa0', '').encode('utf-8').strip()
        item['employee_numbers'] = response.xpath("//div[@class='company-box']/ul/li[1]//strong/text()").extract()[0].replace(u'\xa0', '').encode('utf-8').strip()

        if len(response.xpath("//div[@class='company-box']/ul/li[1]//strong/text()").extract()) > 0:
            item['company_homepage'] = response.xpath("//div[@class='company-box']/ul/li[1]//strong/text()").extract()[0].replace(u'\xa0', '').encode('utf-8').strip()

        item['company_synopsis'] = self.getCompanySynopsis(response)

        item['url'] = response.url

        yield item



    def getCompanySynopsis(self, response):
        synopsis_list =  response.xpath("//div[@class='terminalpage-main clearfix']//div[@class='tab-inner-cont'][2]//p")
        company_synopsis = ''
        for synopsis in synopsis_list:
            if len(synopsis.xpath('.//span/text()')) > 0:
                company_synopsis += synopsis.xpath('.//span/text()').extract()[0].replace(u'\xa0', '').encode('utf-8')
            if len(synopsis.xpath('.//text()')) > 0:
                company_synopsis += synopsis.xpath('.//text()').extract()[0].replace(u'\xa0', '').encode('utf-8')

        return company_synopsis.strip()




    def getPositionInformation(self, response):

        position_information_list = response.xpath("//div[@class='terminalpage-main clearfix']//div[@class='tab-inner-cont'][1]//p")
        position_information_list.pop()
        information = ''.join(position_information_list.extract()).encode('utf-8')
        information = re.sub(r'<([\w\d=\s"-:;]+)([\u4E00 -\u9FA5]*)>|</\w+>', '', information)
        return information.strip()




