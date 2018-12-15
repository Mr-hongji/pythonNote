# -*- coding:utf-8 -*-
'''

xpath 百度贴吧



'''

import urllib2, urllib

from lxml import etree

'''

    使用urllib2获取远程http内容时，时不时出现httplib.IncompleteRead exception错误。

    错误具体为：httplib.IncompleteRead: IncompleteRead(1353 bytes read)

    问题是这个问题一会出现，一会不出现。有时候运行一天也不会出错，有时候10分钟就出错。
    
解决 httplib.IncompleteRead exception 问题 ：

'''

import httplib

httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

header = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.99Safari / 537.36'
    }

header1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }



def pasePageContent(pageContent):
    url = 'http://tieba.baidu.com'
    print(pageContent)
    content = etree.HTML(pageContent)
    print(content)
    tiezi_list = content.xpath("//div[@class='threadlist_lz clearfix']/div[@class='threadlist_title pull_left j_th_tit ']/a/@href")
    print(tiezi_list)
    for data in tiezi_list:
        print(url + data)
        load_suject_page(url + data)




def load_suject_page(url):
    '''
    加载贴吧中的话题页
    :return:
    '''
    try:
        print(url)
        rq = urllib2.Request(url, headers=header1)
        rs = urllib2.urlopen(rq)

        htmlContent = etree.HTML(rs.read())
        img_list = htmlContent.xpath("//div[@class='d_post_content j_d_post_content ']/img[@class='BDE_Image']/@src| //div[@class='d_post_content j_d_post_content ']/img[@class='BDE_Meme']/@src")
        # print(img_list)
        for imgURL in img_list:
            save_img(imgURL)
    except:
        print(url + "加载失败！")



def save_img(imgURL):
    '''
    保存图片
    :param imgURL:
    :return:
    '''
    imgURL =  imgURL.replace("https", "http")

    filename =  'd:/img/' + str(imgURL[-10:])
    try:
        print(filename)
        f = open(filename, 'wb')
        f.write(urllib2.urlopen(imgURL).read())
        f.close()
    except:
        print(filename + '下载失败！')

def load_tieba_main_page(kw):
    '''
    加载贴吧主页
    :return:
    '''

    data = {
        'kw':kw
    }
    main_page_url = 'http://tieba.baidu.com/f?%s' %urllib.urlencode(data)

    print(main_page_url)
    request = urllib2.Request(main_page_url, headers=header)
    response = urllib2.urlopen(request)
    pasePageContent(response.read())

if __name__== '__main__':
    tieba_name = raw_input('输入贴吧名称：')
    load_tieba_main_page(tieba_name)
    # load_suject_page('https://tieba.baidu.com/p/5824256919')
