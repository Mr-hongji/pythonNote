# -*- coding:utf-8 -*-

from selenium import webdriver

from selenium.webdriver.common import keys

driver = webdriver.PhantomJS()

driver.get('http://www.douban.com')

driver.find_element_by_id('form_email').send_keys('lyjn5126@163.com')
driver.find_element_by_id('form_password').send_keys('a25999')

driver.save_screenshot('douban.png')

# 查看截图 输入验证码
driver.find_element_by_id('captcha_field').send_keys('输入验证码')

# 获取登录按钮 点击登录
driver.find_elements_by_class_name('bn-submit').click()

# 退出
driver.quit()