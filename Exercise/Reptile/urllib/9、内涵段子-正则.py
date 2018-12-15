# -*- coding:utf-8 -*-




content = '<dl class="duanzi" id="duanzi_2842" duanzi="2842" duanzi-type="text"><dt>' \
          '<a href="http://www.duanziquan.cn/user/1/" target="_blank"><img src="/skins/member/default/images/face.gif" alt="段子圈"/><i></i></a>' \
          '<p class="duanzi-uname"><a href="http://www.duanziquan.cn/user/1/">段子圈</a><a href="http://www.duanziquan.cn/about/shengjiguize.htm" class="level_icon icon_lv100" title="" target="_blank"></a></p>' \
          '<span class="duanzi-title"><a href="http://www.duanziquan.cn/duanzi/2842.html" target="_blank">炫富的境界有多高</a></span>' \
          '</dt><dd class="content">女：“周末干嘛去了？”<br />男：“和一哥们儿炫富去了。”<br />女：“哦！没看出来你挺有钱的吗？都炫了什么？”<br />男：“还好还好，在狗面前啃骨头；在猫面前下河抓鱼，在蚊子面前献血，在屎壳郎面前拉屎... ...”<br />女：“你可以滚了。”<br></dd><dd class="operation">' \
          '<div class="operation-btn"><a href="javascript:void(0)" rel="nofollow" class="ding" title="顶"><div class="dingcai"><span></span>' \
          '<img src="/css/duanzi/ding.png" /><i>1</i></div></a><span class="operation-line"></span></div><div class="operation-btn">' \
          '<a href="javascript:void(0)" rel="nofollow" class="cai" title="踩"><div class="dingcai"><span></span><img src="/css/duanzi/cai.png" />' \
          '<i>5</i></div></a><span class="operation-line"></span></div><div class="operation-btn">' \
          '<a href="javascript:void(0)" rel="nofollow" class="comment commentClick" title="评论" obj_info="2842-1-list">' \
          '<div class="dingcai"><span></span><i>0</i></div></a><span class="operation-line"></span></div><div class="share">' \
          '<a class="share-ico" title="分享" href="javascript:void(0)" rel="nofollow"></a><div class="share-btn">' \
'<a href="http://www.duanziquan.cn/plus/share.ashx?obj_type=duanzi&obj_id=2842&type=qzone&title=炫富的境界有多高"' \
          ' target="_blank" class="share-qzone" data-cmd="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a></div></div><div class="reward-box">' \
          '</div><div class="buy"></div></dd></dl> '



import urllib2, re, urllib


pageNum = 1


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def saveData(duanziTitle, duanziContent):
    '''
    保存匹配出的段子内容
    :return:
    '''

    filename = 'duanzilist_%d.html' %pageNum

    with open(filename, 'a+') as f:
        f.write(duanziTitle + "<br/>")
        f.write(duanziContent)


def handleData(htmlContent):
    '''

    处理匹配HTML 内容中的段子信息
    :param htmlContent:
    :return:
    '''
    global content

    duanziTitleC = re.compile(r'<span class="duanzi-title">(.*?)</span>')

    duanziContentC = re.compile(r'<dd class="content">(.*?)</dd>')

    print(htmlContent)

    title_list = duanziTitleC.findall(htmlContent)
    content_list = duanziContentC.findall(htmlContent)
    print(content_list)
    for index ,dzc in enumerate(content_list):
        print(index, dzc)

    for index ,dzc in enumerate(title_list):
        print(index, dzc)
        saveData(dzc + '<br/>', content_list[index])



def loadURL():
    '''
    请求页面内容
    :param url: 页面地址
    :return:
    '''
    global pageNum

    switch = True
    while switch:

        print('正在下载第 %d 页数据...' %pageNum)

        requesURL = "http://www.duanziquan.cn/list_" + str(pageNum) + ".html"

        # request = urllib2.Request(requesURL, headers = header)
        # response = urllib2.urlopen(request)

        # handleData(response.read())
        handleData(content)
        action = raw_input('数据下载完成，继续下载输入：回车，退出输入：q')

        if action == 'q':
            switch = False
        else:
            pageNum += 1


if __name__ == '__main__':
    loadURL()
    pass