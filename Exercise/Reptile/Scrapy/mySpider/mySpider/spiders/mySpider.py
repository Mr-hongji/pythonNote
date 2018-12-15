#coding:cp936

# ���� Scrapy ��
import scrapy

# �Լ�����ģ���Ҫ����ĵ��ֶ�
# ���� mySpider ��Ŀ�� items�ļ��е� itcastSpiderItem ��
from ..items import itcastSpiderItem, tencentSpiderItem

# ���� Scrapy �е� Reuest ģ��
from scrapy.http import  Request

'''

items ��ϰ: class itcast (��ȡ���ǲ��ͽ�ʦ��Ϣ)

PipeLines ��ϰ: class tencent (��ȡ��Ѷ��Ƹ��Ϣ)
 
'''

class itcast(scrapy.Spider):

    '''

        Itemss ��ϰ

        ��ȡ���ǲ��͵���ʦ���ݣ�������ְ�ơ���飩

        �Զ��������࣬�̳� scrapy.Spider
        ��ȡ itcast.cn �н�ʦ����Ϣ

    '''

    # ������
    name = 'itcastSpider'

    # ����������ȡ����
    allowed_domains = ['itcast.cn']

    # ��ȡ��url�б�����������ʱ������û�� start_urls �������
    # Ȼ�������б���ȡurl ������ȡ
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#apython']

    # ���淵�����ݵĻص�����, ������������������д��
    def parse(self, response):

        teacher_items = []

        # ʹ�� scrapy���Դ��� xpath ƥ���ȡ������
        teachers =  response.xpath("//div[@class='li_txt']")

        for teacher in teachers:

            # item
            item = itcastSpiderItem()

            # ��ȡ����
            name = teacher.xpath('.//h3/text()').extract()
            # ��ȡְ��
            title = teacher.xpath('.//h4/text()').extract()
            # ��ȡ���
            synopsis = teacher.xpath('.//p/text()').extract()

            # UnicodeEncodeError: 'gbk' codec can't encode character u'\xa0' in position 9 ����
            # ����취һ�� �ڶ�unicode�ַ�����ʱ�����ignore�����������޷��޷�������ַ��������Ϳ�����������ΪGBK��
            item['name'] = name[0].encode("gbk", 'ignore')
            item['title'] = title[0].encode("gbk", 'ignore')
            item['synopsis'] = synopsis[0].encode("gbk", 'ignore')


            # ����취���� �滻��u'\xa0'
            # item['name'] = name[0].replace(u'\xa0', u' ').encode("gbk")
            # item['title'] = title[0].replace(u'\xa0', u' ').encode("gbk")
            # item['info'] = info[0].replace(u'\xa0', u' ').encode("gbk")

            teacher_items.append(item)

        # Ҫʹ�� items �����ݱ��浽�ļ��У���Ҫ return ����
        # ���ص�����ʹ�� start.py �ļ��е�exect ִ������ ��
        # scrapy scrawl itcast -o itcast.jsom ����������� itcast.json �ļ���
        return teacher_items



class tencent(scrapy.Spider):

    '''

        PipeLines ��ϰ ��ȡ��Ѷ��Ƹ��Ϣ

    '''
    name = 'tencentSpider'

    allowed_domains = ['tencent.com']

    url = 'https://hr.tencent.com/position.php?start='

    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):
        print(response.body)
        # ��ȡְλ��Ϣ�б�����
        # ���⣺���������ʹ�� xpath help ���� �� tbody ����ƥ�����ݣ� �ڴ�����ʹ�� xpath ��ƥ�䲻������ �磺 //tbody/tr[@class='even']| //tbody/tr[@class='odd']
        # �𰸣����������table��ǩ�����tbody��ע����chrome��������Զ�������������������ԭ������Ϊ��������html�ı�����һ���Ĺ淶�� ��
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

            # ʹ�� yield ���ص����ݻᾭ�� pipelines
            yield item

            # ʹ��return ���ݲ��ᾭ�� pipelines
            # return item

        if self.offset < 349:
            self.offset += 1

        yield  scrapy.Request(self.url + str(self.offset), callback=self.parse)
