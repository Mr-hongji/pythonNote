# -*- coding:utf-8 -*-
'''百度贴吧'''

import urllib2,urllib,os

def writeFile(html, filename):

    print('正在保存数据...')

    '''
    
        python直接读取中文路径的文件时失败，可做如下处理：
        
        inpath = 'D:/work/yuanxx/在线导航/驾车导航/walk_log/20130619_172355.txt'
        uipath = unicode(ipath , "utf8")
        
        然后用"uipath"经过编码后的路径去open()即可:
        
        fin = open(uipath)
    
    '''
    uipath = unicode(filename, "utf8")

    with open(uipath, 'w') as f:
        f.write(html)

def startLoad(requestUrl):

    req_headers ={
    'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.99Safari / 537.36',
    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8'
    }

    request = urllib2.Request(requestUrl, headers = req_headers )
    response = urllib2.urlopen(request)

    return response.read()


def cerateRequestUrl(requestUrl, wd, startpage, endpage):
    kw = {'kw':wd}
    kw = urllib.urlencode(kw)

    for i in range(startpage, endpage + 1):
        pn = (i - 1) * 50
        requestUrl = requestUrl + kw + "&pn=" + str(pn)
        filename = '第'+ str(i) + '页.html'
        print('正在下载第'+ str(i) + '页数据...')

        html = startLoad(requestUrl)

        writeFile(html, filename)



if __name__ == '__main__':
    requestUrl = 'http://tieba.baidu.com/f?'
    wd = raw_input('请输入贴吧名称：')
    startPage = raw_input('请输入开始页：')
    endPage = raw_input('请输入结束页：')

    cerateRequestUrl(requestUrl, wd, int(startPage), int(endPage))

# 'http://tieba.baidu.com/f?kw=penbeat&ie=utf-8&pn=0'

