# -*- coding:utf-8 -*-
'''

使用多线程爬取糗事百科

'''

import urllib2, json

from Queue import  Queue

from threading import Thread

from lxml import etree



class collectionThread(Thread):

    def __init__(self, threadname, pageQueue, htmlQueue):
        super(collectionThread, self).__init__()
        self.threadname = threadname
        self.pageQueue = pageQueue
        self.htmlQueue = htmlQueue

    def run(self):

        print(self.name + '开始...')
        
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        while not self.pageQueue.empty():
            url = self.pageQueue.get()

            request = urllib2.Request(url, headers=header)
            response = urllib2.urlopen(request)

            html = response.read()

            self.htmlQueue.put(html)

        print(self.name + '结束...')



class paseThread(Thread):

    def __init__(self, name, htmlQueue, filename):
        super(paseThread, self).__init__()
        self.name = name
        self.htmlQueue = htmlQueue
        self.filename = filename

    def run(self):

         print(self.name + '开始...')

         while not self.htmlQueue.empty():
            html = self.htmlQueue.get()
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
                    'vote': node.xpath(".//span[@class ='stats-vote']/i[@class='number']")[0].text,
                     # 获取评论数
                    'comment': node.xpath(".//span[@class='stats-comments']//i[@class='number']")[0].text,
                }

                self.filename.write(json.dumps(tiezi, ensure_ascii = False).encode('utf-8') + '\n')

         print(self.name + '结束...')



if __name__=='__main__':

    pageQueue = Queue(10)
    dataQueue = Queue()
    htmlQueue = Queue()

    collectionThreadName = ['采集线程1', '采集线程2', '采集线程3']

    paseThreadName = ['解析线程1', '解析线程2', '解析线程3']

    collectionThreads = []
    paseThreads = []

    filename = open('qiushibaike1.json', 'a')

    for i in range(1,11):
        url = 'https://www.qiushibaike.com/8hr/page/%d/' % i
        pageQueue.put(url)

    for threadName in collectionThreadName:
        ct = collectionThread(threadName, pageQueue, htmlQueue)
        collectionThreads.append(ct)
        ct.start()

    for thread in collectionThreads:
        thread.join()

    print('数据采集完成')

    for ptname in paseThreadName:
        pt = paseThread(ptname, htmlQueue, filename)
        paseThreads.append(pt)
        pt.start()

    for pthread in  paseThreads:
        pthread.join()

    print('数据解析完成')

    filename.close()



