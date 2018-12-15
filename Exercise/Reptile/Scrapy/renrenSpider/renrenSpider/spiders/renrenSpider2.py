# -*- coding:utf-8 -*-

'''

使用 cookies 模拟登录

 在浏览器中输入账号密码进行登录，然后复制 cookies 信息，使用 这个 cookies 信息 直接访问登录后关注的好友主页


 这个方法是最后的无奈之举， 100% 成功

'''

import scrapy

class renrenSpider2(scrapy.Spider):

    name = 'renren2'

    allowed_domains = ['renre.com']

    start_urls = [
        'http://www.renren.com/256450404/profile',
        'http://www.renren.com/250987359/profile',
        'http://www.renren.com/435297442/profile'
    ]

    cookies = {
        'anonymid':'jk86klgv9ei788',
        '_r01_':'1',
        '__utma':'151146938.1595563435.1532949565.1532949565.1532949565.1',
        '__utmz':'151146938.1532949565.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'ln_uact':'lyjn5126@163.com',
        'ln_hurl':'http://hdn.xnimg.cn/photos/hdn421/20130107/1630/original_F0AZ_5dbc00002b23111a.jpg',
        'BDTUJIAID':'6ca31eaa63ed64f10f13081b95a7f0d0',
        'wp':'0',
        'depovince':'GW',
        'ick_login':'3e165330-8538-4eb3-a50c-b7a9f698e3b8',
        'jebe_key':'26c998f3-4d6f-47b4-b36d-91c7814dd7c1%7Cd5560ba4d708e19e54f33546c67f1c40%7C1532949753696%7C1%7C1534392263541',
        'first_login_flag':'1',
        'wp_fold':'0',
        'jebecookies':'a41fc18f-83ce-43ea-a719-c37d026e77ed|||||',
        '_de':'57C1ED38ADB63EF444B0A57815E527E7696BF75400CE19CC',
        'p':'b6ef152fa2c9adcea19669f138fc52a54',
        't':'9a0e51d157a1ee51ca322e81f7b397214',
        'societyguester':'9a0e51d157a1ee51ca322e81f7b397214',
        'id':'523562114',
        'xnsid':'bd4cf00c',
        'ver':'7.0',
        'loginfrom':'null'
    }

    pageName = 3

    def start_requests(self):
        url = 'http://www.renren.com/256450404/profile'

        yield scrapy.FormRequest(url = url, cookies = self.cookies, meta = {'cookiejar' : 1})


    def parse(self, response):
        global pageName

        self.pageName += 1

        with open(str(self.pageName) + '.html', 'w') as f:
            f.write(response.body)