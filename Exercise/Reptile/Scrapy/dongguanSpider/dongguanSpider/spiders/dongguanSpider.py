#-*- coding:utf-8 -*-

'''
linux use :
 

'''

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import DongguanspiderItem

import sys

reload(sys)
sys.setdefaultencoding('utf8')

class dongguanSpider(CrawlSpider):

    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report']

    linkEx =  LinkExtractor(allow=(r'page=\d+'))

    linkEx1 = LinkExtractor(allow=(r'/\d+/\d+.shtml'))

    rules = (
        Rule(linkEx, follow = True),
        Rule(linkEx1, follow = True, callback = 'dongguanParse')
    )

    def dongguanParse(self, response):

        '''

        :param response:
        :return:
        '''

        # extract() 方法：把返回的数据转换成 unicode 编码格式的 list

        item = DongguanspiderItem()

        title_nmber = response.xpath("//div[@class='pagecenter p3']//strong[@class='tgray14']/text()").extract()[0]

        nickname_time = response.xpath("//div[@class='pagecenter p3']//div[@class='cright']/p/text()").extract()[0]

        item['q_title'] = title_nmber.split('提问：')[-1].split('编号:')[0].replace(u'\xa0', '').strip().encode('utf-8')

        item['q_number'] = title_nmber.strip().split('提问：')[-1].split('编号:')[1].replace(u'\xa0', '').strip().encode('utf-8')

        # 内容中没有图片 则取 div[@class ='c1 text14_2'] 中的 text
        # 内容中有图片 则取 div[@class='contentext'] 中的 text
        div_contentext = response.xpath("//div[@class='pagecenter p3']//div[@class ='contentext']/text()")
        div_c1_text14_2 = response.xpath("//div[@class='pagecenter p3']//div[@class ='c1 text14_2']/text()")

        # 内容中会存在换行问题 <br> ,匹配出的数据集合 len > 1 所以使用 ''.join(div_contentext.extract()) 来拼接list
        if len(div_contentext) > 0:
            item['q_content'] = ''.join(div_contentext.extract()).strip(u'\xa0').encode('utf-8')
        else:
            item['q_content'] = ''.join(div_c1_text14_2.extract()).strip(u'\xa0').encode('utf-8')

        item['q_state'] = response.xpath("//div[@class='pagecenter p3']//div[@class='cleft']/span/text()").extract()[0].replace(u'\xa0', '').strip().encode('utf-8')

        item['q_nickname'] = nickname_time.split('网友：')[-1].split('发言时间：')[0].replace(u'\xa0', '').strip().encode('utf-8')

        item['q_time'] = nickname_time.split('网友：')[-1].split('发言时间：')[1].replace(u'\xa0', '').strip().encode('utf-8')

        item['q_url'] = response.url
        return item


