# -*- coding:utf-8 -*-
'''

知识点：

    1、使用 json 解析数据
    2、使用 xpath 进行模糊匹配

'''

import urllib2, json

from lxml import etree

import sys

reload(sys)
sys.setdefaultencoding('utf8')

header = {

'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

for i in range(1, 6):

    url = 'https://www.qiushibaike.com/8hr/page/%d/' %i

    request = urllib2.Request(url, headers = header)

    response = urllib2.urlopen(request)

    html = response.read()

    content = etree.HTML(html)

    # 使用模糊匹配获取整个段子元素
    # 查询 属性 id 值中包含 qiushi_tag_ 的
    content_list = content.xpath("//div[contains(@id,'qiushi_tag_')]")

    for node in content_list:

        tiezi = {
            # 获取昵称
            'nikname': node.xpath(".//h2")[0].text,

            # 获取段子内容
            'tieziContent': node.xpath(".//div[@class ='content']/span")[0].text,

            # 获取帖子内容中的图片地址
            'tieziImg': node.xpath(".//div[@class ='thumb']/a/img/@src"),

            # 获取投票数
            'vote':  node.xpath(".//span[@class ='stats-vote']/i[@class='number']")[0].text,

            # 获取评论数
            'comment': node.xpath(".//span[@class='stats-comments']//i[@class='number']")[0].text,

        }


        with open('qiushibaike.json','a') as f:
            f.write(json.dumps(tiezi, ensure_ascii = False).encode('utf-8') + '\n')
















