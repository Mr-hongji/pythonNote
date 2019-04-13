# -*- coding:utf-8 -*-

class page(object):
    '''
    分页
    '''
    def __init__(self, sumNum, currentPage, pageSize = 1):
        '''
        :param sumNum: 数据总条数
        :param pageSize: 每页显示条数
        :param currentPage: 当前页数
        '''
        self.sumNum = sumNum
        self.pageSize = pageSize
        self.currentPage = currentPage

        if currentPage <= 0:
            self.currentPage = 1
        elif currentPage >= self.pageCount:
            self.currentPage = self.pageCount

    @property
    def page_size(self):
        return self.pageSize

    @property
    def pageCount(self):
        '''
        总页数
        :return:
        '''
        if self.sumNum % self.pageSize > 0:
            page_count = (self.sumNum / self.pageSize) + 1
        else:
            page_count = self.sumNum / self.pageSize

        return page_count

    @property
    def prePage(self):
        '''
        上一页
        :return:
        '''
        pre_page = self.currentPage - 1
        if pre_page < 1:
            pre_page = 1
        return pre_page

    @property
    def nextPage(self):
        '''
        下一页
        :return:
        '''
        next_page = self.currentPage + 1
        if next_page > self.pageCount:
            next_page = self.pageCount

        return next_page

    @property
    def pageNum(self):

        '''
        上一页和下一页 的中间页码 （显示10个）
        :return:
        '''

        page_nums = []
        # 当前页 前后显示5个数字页码
        limitNum = 5

        # 如果当前页 - limitNum < 1
        if self.currentPage - limitNum < 1:
            page_nums = range(1, limitNum * 2 + 1)

        # 如果当前页 + limitNum > 总页数
        elif self.currentPage + limitNum > self.pageCount:
            page_nums = range(self.pageCount - (limitNum * 2) + 1, self.pageCount + 1)
        else:
            page_nums = range(self.currentPage - limitNum, self.currentPage + limitNum)

        return page_nums

    @property
    def paginatorResult(self):
        hstr = '<a class="paginator_btn" href="getArticle.html?page=' + str(self.prePage) + '">上一页</a>'
        for n in self.pageNum:
            if n == self.currentPage:
                hstr += ' <a class="paginator_btn" href="getArticle.html?page=' + str(n) + '" >' + str(n) + '</a>'
            else:
                hstr += ' <a class="paginator_btn" href="getArticle/?page=' + str(n) + '">' + str(n) + '</a>'

        hstr += ' <a class="paginator_btn" href="paginator/?page=' + str(self.nextPage) + '">下一页</a> '

       # hstr += str(self.currentPage) + '/' + str(self.pageCount)
        return hstr
