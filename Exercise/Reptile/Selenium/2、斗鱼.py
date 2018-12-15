# -*- coding:utf-8 -*-

from selenium import webdriver
from lxml import etree
from bs4 import BeautifulSoup

import urllib2


driver = None
pageNum = 0
HAS_NEXT_PAGE = True

def go_action(gopage_num):

    '''
     跳转页面 函数
    :param gopage_num: 跳转到第几页
    :return:
    '''

    # 获取页面 跳转输入框，设置跳转 页码
    driver.find_element_by_class_name('jumptxt').send_keys(gopage_num)

    # 查找 go 按钮，执行点击
    driver.find_element_by_class_name('shark-pager-submit').click()

    # 等待 3 秒
    time.sleep(3)

    # 保存页面截图
    driver.save_screenshot('douyu1.png')

    # 解析页面数据
    parseData(driver.page_source)


def parseData(content):
    global HAS_NEXT_PAGE

    # print(content)
    try:

        # HTML源码 按lxml 格式解析
        bs = BeautifulSoup(content, 'lxml')

        # 查找 下一页按钮是否被禁用
        # 'class': 'shark-pager-next shark-pager-disable shark-pager-disable-next' 下一个按钮禁用时的 class 样式
        fresult = bs.find('a', attrs={'class': 'shark-pager-next shark-pager-disable shark-pager-disable-next'})

        '''
            用下面的方式获取数据，不严谨，容易出现获取出的 房间数列表 和 房间人数列表个数不匹配

        '''

        # 如果找到 下一步按钮是禁用 则停止循环点击下一页
        if fresult:
            HAS_NEXT_PAGE = False

        # 获取 房间名称
        room_names = bs.find_all('a', attrs={'class':'play-list-link'})

        # 获取直拨房间人数
        view_numbers = bs.find_all('span',attrs={'class':'dy-num fr'})

        print(str(pageNum) + ', ' + str(len(room_names)) + ', ' + str(len(view_numbers)))

        for i, value in enumerate(room_names):
            print(str(i) + u', 房间人数: ' + view_numbers[i].text + u', 房间名称： ' + value.get('title'))

    except Exception, e:
        print e




def loadHtmlPage():
    global  pageNum

    while HAS_NEXT_PAGE:
        try:
            time.sleep(3)
            pageNum += 1
            driver.find_element_by_class_name('shark-pager-next').click()
            parseData( driver.page_source)
        except:
            pass


import time

if __name__ == '__main__':
    pageNum += 1
    url = 'https://www.douyu.com/directory/all'

    driver = webdriver.PhantomJS()

    # 请求 url
    driver.get(url)

    # 保存页面截图
    driver.save_screenshot('douyu.png')

    # 解析数据 driver.page_source：去除页面源码
    parseData(driver.page_source)

    loadHtmlPage()







