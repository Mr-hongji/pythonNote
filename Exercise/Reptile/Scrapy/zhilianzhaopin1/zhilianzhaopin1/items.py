# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ZhilianzhaopinItem(Item):
    # 职位名称
    position_name = Field()
    # 工作地点
    work_place = Field()
    # 工作年限
    working_seniority = Field()
    # 学历要求
    educational_requirements = Field()
    # 薪资
    salary = Field()
    # 职位信息
    position_information = Field()
    # 职位福利
    position_welfare = Field()
    # 公司名称
    company_name = Field()
    # 公司行业
    company_industry = Field()
    # 公司性质
    company_nature = Field()
    # 公司人数
    employee_numbers = Field()
    # 公司主页
    company_homepage = Field()
    # 公司简介
    company_synopsis = Field()

    url = Field()
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()