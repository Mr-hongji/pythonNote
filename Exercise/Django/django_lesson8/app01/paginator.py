# -*- coding:utf-8 -*-
class paginator(object):
    '''
    page_num 共多少页
    page_size 每页显示的条数
    sum 数据总条数
    '''
    def __init__(self, current_page, sum, page_size):
        self.current_page = current_page
        self.sum = sum
        self.page_size = page_size

        if current_page <= 0:
            self.current_page = 1
        elif current_page >= self.pageCount:
            self.current_page = self.pageCount



    @property
    def pageCount(self):
        '''
        总页数
        :return:
        '''
        if self.sum % self.page_size > 0:
            page_count = (self.sum / self.page_size) + 1
        else:
            page_count = self.sum / self.page_size

        return page_count

    @property
    def prePage(self):
        '''
        上一页
        :return:
        '''
        pre_page = self.current_page - 1
        if pre_page < 1:
            pre_page = 1
        return pre_page

    @property
    def nextPage(self):
        '''
        下一页
        :return:
        '''
        next_page = self.current_page + 1
        if next_page > self.pageCount:
            next_page = self.pageCount

        return next_page

    # @property
    # def pageNum(self):
    #     page_nums = []
    #     for num in range(1, 6):
    #         if (self.current_page - num > 0):
    #             page_nums.append(self.current_page - num)
    #
    #     page_nums.reverse()
    #
    #     page_nums.append(self.current_page)
    #
    #     for num in range(1, 11 - len(page_nums)):
    #         if self.current_page + num <= self.pageCount:
    #             page_nums.append(self.current_page + num)
    #
    #     return page_nums

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
        if self.current_page - limitNum < 1:
            page_nums = range(1, limitNum * 2 + 1)

        # 如果当前页 + limitNum > 总页数
        elif self.current_page + limitNum > self.pageCount:
            page_nums = range(self.pageCount - (limitNum  * 2) + 1, self.pageCount + 1)
        else:
            page_nums = range(self.current_page - limitNum, self.current_page + limitNum)

        return page_nums

    @property
    def paginatorResult(self):
        hstr = '<a href="paginator.html?page='+str(self.prePage)+'">上一页</a>'
        for n in self.pageNum:
            if n == self.current_page:
                hstr += ' <a href="paginator.html?page='+ str(n) +'" style="font-size: 24px">'+ str(n) +'</a>'
            else:
                hstr += ' <a href="paginator.html?page=' + str(n) + '">' + str(n) + '</a>'

        hstr += ' <a href="paginator.html?page='+str(self.nextPage)+'">下一页</a> '

        hstr += str(self.current_page) + '/' + str(self.pageCount)
        return hstr


    def paginatorResult_BootStrap(self):
        '''
        使用 bootstrap 分页插件
        :return:
        '''
        boots = '<nav aria-label="Page navigation">'
        boots += '<ul class="pagination">'
        if self.current_page == 1:
            boots += '<li class="disabled"><a href="paginator.html?page='+str(self.prePage)+'" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        else:
            boots += '<li><a href="paginator.html?page=' + str(self.prePage) + '" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'

        for n in self.pageNum:
            if n == self.current_page:
                boots += '<li class="active"><a href="paginator.html?page=' + str(n) + '" >' + str(n) + '</a></li>'
            else:
                boots += '<li><a href="paginator.html?page=' + str(n) + '">' + str(n) + '</a></li>'

        if self.current_page == self.pageCount:
            boots += '<li class="disabled"><a href="paginator.html?page='+str(self.nextPage)+'" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        else:
            boots += '<li><a href="paginator.html?page=' + str(self.nextPage) + '" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'

        boots += '<li><span aria-hidden="true">' + str(self.current_page) + ' / ' + str(self.pageCount) + '</span></li>'

        boots += '</ul> &nbsp;' \
                 '<ul class="pagination">' \
                 '<li>' \
                 '<a href="#" style="height: 34px;padding: 0px">' \
                 '<input type="text" id="goPageNum" style="height: 31px; width: 60px; border: none; font-size: 14px;' \
                 ' text-align: center;" placeholder="跳转到">' \
                 '</a>' \
                 '</li>' \
                 '<li>' \
                 '<a href="#">' \
                 '<span aria-hidden="true" class="goBtn">go</span></a></li></ul>' \
                 '</nav>'

        return boots

