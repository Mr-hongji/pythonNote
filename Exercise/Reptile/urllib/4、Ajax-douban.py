# -*- coding:utf-8 -*-

'''

获取 豆瓣电影列表数据

    豆瓣电影列表加载使用的是 Ajax 方式，Ajax 方式返回的数据都是 Json 格式

'''

import urllib, urllib2

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


movies = {
    '11':'剧情',
    '24':'喜剧',
    '5':'动作',
    '13':'爱情',
    '17':'科幻',
    '25':'动画',
    '10':'悬疑',
    '19':'惊悚',
    '20':'恐怖',
    '1':'纪录片',
    '23':'短片'
}

def requestURL(pageSize, pageCount, type):
    '''
    :param pageSize: 每页显示条数
    :param pageCount: 总共查询多少页数据
    :param type: 影片类型
    :return:
    '''

    for i in range(1, int(pageCount) + 1):

        requrl = 'https://movie.douban.com/j/chart/top_list'

        start = (i - 1) * int(pageSize)
        data = {
            'type': type,
            'interval_id': '100:90',
            'action': '',
            'start': start,
            'limit': pageSize
        }

        data = urllib.urlencode(data)

        request = urllib2.Request(requrl, data = data, headers = headers)

        response = urllib2.urlopen(request)

        print(response.read())


if __name__ == '__main__':
    pageCount = raw_input('输入要抓取数据的总页数：')
    pageSize = raw_input('输入每次抓取的数据条数：')

    print('类型：')
    for k, v in movies.iteritems():
        print('%s: %s' %(k, v))

    movieType = raw_input('请输入电影类型：')

    requestURL(pageSize, pageCount, movieType)