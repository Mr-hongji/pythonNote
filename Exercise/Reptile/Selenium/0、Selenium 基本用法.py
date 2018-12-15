# -*- coding:utf-8 -*-
'''

运行错误：
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
  warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '


大概意思：selenium已经放弃PhantomJS，了，建议使用火狐或者谷歌无界面浏览器。

如果要取消错误，可以降低 Selenium 的版本


查找页面元素：

    返回一个元素：

        find_element_by_id # id定位
        find_element_by_name  # name定位
        find_element_by_xpath # xpath定位

        # （查找元素的链接文本）
        find_element_by_link_text # link定位

        # （查找元素的链接的部分文本）
        find_element_by_partial_link_text # partial_link定位

        find_element_by_tag_name # tag定位
        find_element_by_class_name # class定位
        find_element_by_css_selector # css定位


    复数形式：

        find_elements_by_name
        find_elements_by_xpath
        find_elements_by_link_text
        find_elements_by_partial_link_text
        find_elements_by_tag_name
        find_elements_by_class_name
        find_elements_by_css_selector



    这两种就是快失传了的
        find_element(self, by='id', value=None)
        find_elements(self, by='id', value=None)


    1.element方法定位到是是单数，是直接定位到元素

    2.elements方法是复数，这个学过英文的都知道，定位到的是一组元素，返回的是list队列



元素操作方法：

    clear 清除元素的内容
    send_keys 模拟按键输入
    click 点击元素
    submit 提交表单
    quit 退出浏览器


获取常用的值:

    size 获取元素的尺寸
    text 获取元素的文本
    get_attribute(name) 获取属性值
    location 获取元素坐标，先找到要获取的元素，再调用该方法
    page_source 返回页面源码
    driver.title 返回页面标题
    current_url 获取当前页面的URL
    is_displayed() 设置该元素是否可见
    is_enabled() 判断元素是否被使用
    is_selected() 判断元素是否被选中
    tag_name 返回元素的tagName

'''

from selenium import webdriver

import time

driver = webdriver.PhantomJS()

driver.get('http://www.baidu.com/')

print(driver.title)

print(driver.page_source)

element = driver.find_element_by_name('wd')
element.send_keys('phantomjs')

driver.save_screenshot('phantomjs.png')

driver.find_element_by_id("kw").clear()


driver.find_element_by_id("kw").send_keys(u'美女')
driver.find_element_by_id('su').click()
driver.save_screenshot('meinv.png')


element = driver.find_element_by_class_name("s_btn")

print('sss')

driver.quit()

'''
    <div class="cheese"><span>Cheddar</span></div><div class="cheese"><span>Gouda</span></div>
'''
